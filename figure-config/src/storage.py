from sqlalchemy import create_engine, Column, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import duckdb
import pandas as pd
import logging
from typing import List, Optional


Base = declarative_base()

class PaperRecord(Base):
    __tablename__ = 'papers'
    pmcid = Column(String, primary_key=True)
    pmid = Column(String)
    title = Column(Text)
    abstract = Column(Text)
    captions = Column(JSON)

class Storage:
    def __init__(self, db_path: str, csv_path: str):
        self.engine = create_engine(f'duckdb:///{db_path}')
        self.csv_path = csv_path
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_paper(self, paper: dict):
        with self.Session() as session:
            record = PaperRecord(**paper)
            session.merge(record)
            session.commit()
        # Append to CSV
        try:
            df = pd.DataFrame([paper])
            df.to_csv(self.csv_path, mode='a', index=False, header=not pd.io.common.file_exists(self.csv_path))
            logging.info(f"Saved paper {paper['pmcid']} to CSV")
        except Exception as e:
            logging.error(f"Failed to save paper {paper['pmcid']} to CSV: {e}")

    def query_papers(self, pmcids: List[str] = None) -> List[dict]:
        with self.Session() as session:
            query = session.query(PaperRecord)
            if pmcids:
                query = query.filter(PaperRecord.pmcid.in_(pmcids))
            return [
                {
                    'pmcid': r.pmcid,
                    'pmid': r.pmid,
                    'title': r.title,
                    'abstract': r.abstract,
                    'captions': r.captions
                } for r in query.all()
            ]