import argparse
import logging
from src.ingestion import IngestionPipeline, DataSource, Storage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmcids", nargs="+", required=True, help="List of PMC IDs")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(f"Starting ingestion for PMCIDs: {args.pmcids}")

    # Set your own URLs and API key here
    bioc_pmc_url = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json"
    pubtator3_url = "https://www.ncbi.nlm.nih.gov/research/pubtator3/api"
    api_key = "demo"  # Replace with your real API key if needed

    data_source = DataSource(bioc_pmc_url, pubtator3_url, api_key)
    storage = Storage(db_path="output/json", csv_path="output/csv")
    pipeline = IngestionPipeline(data_source, storage)

    pipeline.run(pmcids=args.pmcids)


if __name__ == "__main__":
    main()
