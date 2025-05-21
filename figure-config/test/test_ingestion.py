import pytest
from src.ingestion import DataSource, IngestionPipeline
from src.storage import Storage
from unittest.mock import patch

@pytest.fixture
def mock_data_source():
    class MockDataSource:
        def fetch_paper(self, pmcid):
            return {
                'pmcid': pmcid,
                'pmid': None,
                'title': 'Test Paper',
                'abstract': 'Test Abstract',
                'captions': [{'figure_id': 'fig1', 'caption': 'Test Caption', 'url': None, 'entities': []}]
            }
        def fetch_entities(self, text):
            return []
    return MockDataSource()

def test_ingestion_pipeline(mock_data_source, tmp_path):
    storage = Storage(str(tmp_path / 'test.db'))
    pipeline = IngestionPipeline(mock_data_source, storage)
    summary = pipeline.ingest(['PMC123'])
    assert summary['success'] == 1
    assert summary['failed'] == 0