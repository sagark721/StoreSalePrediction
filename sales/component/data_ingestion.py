from sales.entity.artifact_entity import DataIngestionArtifact
from sales.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> DataIngestionArtifact :

        self.data_ingestion_config = data_ingestion_config

    def download_dataset():
        pass

    def split_dataset_into_train_and_test():
        pass

    def initiate_data_ingestion():
        pass
