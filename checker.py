from sales.component.data_ingestion import DataIngestion
from sales.config.configuration import Configuration


data_ingestion_config= Configuration().get_data_ingestion_config()

DataIngestion(data_ingestion_config).download_dataset()