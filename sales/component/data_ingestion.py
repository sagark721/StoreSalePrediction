from sales.entity.artifact_entity import DataIngestionArtifact
from sales.entity.config_entity import DataIngestionConfig
from sales.logger import logging
import os
import urllib.request


ingested_data_dir= "Ingested_data"
ingested_train_dir= "Train_data"
ingested_test_dir= "Test_data" 


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> DataIngestionArtifact :

        self.data_ingestion_config = data_ingestion_config
        

    def download_dataset(self):
        logging.info(f"Downloading Dataset")
        dataset_download_url=dataset_download_url
        #test_dataset_download_url = test_dataset_download_url

        dataset_dir = ingested_data_dir
        os.makedirs(dataset_dir,exist_ok=True)

        train_dataset_file_name = os.path.basename(dataset_download_url)
        train_dataset_file_path = os.path.join(dataset_dir,train_dataset_file_name)

        #test_dataset_file_name =os.path.basename(test_dataset_download_url)
        #test_dataset_file_path = os.path.join(dataset_dir,test_dataset_file_name)

        urllib.request.urlretrieve(dataset_download_url,train_dataset_file_path)
    
    
        #urllib.request.urlretrieve(test_dataset_download_url,test_dataset_file_path)
        
        return train_dataset_file_path
        

    def split_dataset_into_train_and_test():
        pass

    def initiate_data_ingestion():
        pass
