from sales.utils.utils import read_yaml_file
from sales.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from sales.constant import *
import os


class Configuration:

    def __init__(self,config_info):
        self.config_info = read_yaml_file(CONFIG_FILE_PATH)
        self.training_pipeline_config = self.get_training_pipeline_config()

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:

        artifact_dir = self.training_pipeline_config.artifact_dir
        data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR_NAME_KEY)

        data_ingestion_config_info=os.path.join(ROOT_DIR,data_ingestion_artifact_dir,self.config_info[DATA_INGESTION_CONFIG_KEY])
        dataset_download_url=data_ingestion_config_info[dataset_download_url]
        test_dataset_download_url=data_ingestion_config_info[DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY]

        ingested_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_INGESTED_DATA_DIR_KEY])
        ingested_train_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_INGESTED_TRAIN_DATA_DIR_KEY])
        ingested_test_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_config_info[DATA_INGESTION_INGESTED_TEST_DATA_DIR_KEY])



        data_ingestion_config=DataIngestionConfig(

        dataset_download_url=dataset_download_url,
        test_dataset_download_url=test_dataset_download_url,
        ingested_data_dir=ingested_data_dir,
        ingested_train_dir=ingested_train_dir,
        ingested_test_dir=ingested_test_dir)

        return data_ingestion_config


    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

        artifact_dir=os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
        )
        training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)

        return training_pipeline_config


