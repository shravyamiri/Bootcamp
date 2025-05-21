import os
import json
import csv
import logging
import requests
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)


class DataSource:
    def __init__(self, bioc_pmc_url: str, pubtator3_url: str, api_key: str):
        self.bioc_pmc_url = bioc_pmc_url
        self.pubtator3_url = pubtator3_url
        self.api_key = api_key

    def fetch(self, pmcid: str) -> Dict[str, Any]:
        url = f"{self.bioc_pmc_url}/{pmcid}?api_key={self.api_key}"
        logging.info(f"Requesting URL: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data for {pmcid}: {response.status_code}")

        data = response.json()

        # Handle if response is a list or a dict
        if isinstance(data, dict) and "documents" in data:
            return {"pmcid": pmcid, "data": data}
        elif isinstance(data, list):
            return {"pmcid": pmcid, "data": {"documents": data}}  # wrap list as documents
        else:
            raise Exception(f"Unexpected response format for {pmcid}: {type(data)}")


class Storage:
    def __init__(self, db_path: str, csv_path: str):
        self.db_path = db_path
        self.csv_path = csv_path
        os.makedirs(db_path, exist_ok=True)
        os.makedirs(csv_path, exist_ok=True)

    def save(self, record: Dict[str, Any]):
        pmcid = record.get("pmcid", "unknown")
        document = record.get("data", {}).get("documents", [])[0] if record.get("data", {}).get("documents") else {}
        title = document.get("passages", [{}])[0].get("text", "N/A")  # Get title-like text if possible
        passages = document.get("passages", [])

        # Save full JSON
        json_path = os.path.join(self.db_path, f"{pmcid}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(record["data"], f, indent=4)
        logging.info(f"Saved JSON to {json_path}")

        # Save summary CSV
        csv_path = os.path.join(self.csv_path, "summary.csv")
        with open(csv_path, mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["pmcid", "title", "passages_count"])
            writer.writerow([pmcid, title[:100], len(passages)])  # Truncate title if too long
        logging.info(f"Saved summary to {csv_path}")


class IngestionPipeline:
    def __init__(self, data_source: DataSource, storage: Storage):
        self.data_source = data_source
        self.storage = storage

    def run(self, pmcids: List[str]):
        logging.info("Running ingestion pipeline...")
        for pmcid in pmcids:
            try:
                logging.info(f"Fetching data for {pmcid}...")
                data = self.data_source.fetch(pmcid)
                self.storage.save(data)
            except Exception as e:
                logging.error(f"Error processing {pmcid}: {e}")
