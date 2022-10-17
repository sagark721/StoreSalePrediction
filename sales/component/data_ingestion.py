from sales.entity.artifact_entity import DataIngestionArtifact
from sales.entity.config_entity import DataIngestionConfig
from sales.logger import logging
import os
import urllib.request





class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> DataIngestionArtifact :
        try:

            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise (e)
        
        

    def download_dataset(self):
        try:
            logging.info(f"Downloading Dataset")

            train_dataset_url=self.data_ingestion_config.train_dataset_download_url
            test_dataset_url=self.data_ingestion_config.test_dataset_download_url

            dataset_dir=self.data_ingestion_config.ingested_data_dir
            os.makedirs(dataset_dir,exist_ok=True)

            train_dataset_file_name = os.path.basename(train_dataset_url)
            test_dataset_file_name = os.path.basename(test_dataset_url)

            train_dataset_file_path = os.path.join(dataset_dir,train_dataset_file_name)
            test_dataset_file_path = os.path.join(dataset_dir,test_dataset_file_name)

            train_dataset=urllib.request.urlretrieve(train_dataset_url,train_dataset_file_path)
            test_dataset=urllib.request.urlretrieve(test_dataset_url,test_dataset_file_path)

            data_ingestion_artifact=DataIngestionArtifact(train_dataset_file_path=train_dataset_file_path,
            test_dataset_file_path=test_dataset_file_path,is_data_ingested=True,message="Data Ingested Successfully")

            return data_ingestion_artifact
        
        except Exception as e:
            raise(e)



    def initiate_data_ingestion(self):
        try:
            return self.download_dataset()
        except Exception as e:
            raise (e)
