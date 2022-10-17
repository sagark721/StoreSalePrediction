import os

ROOT_DIR = os.getcwd()
CONFIG_FILE_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_FILE_DIR,CONFIG_FILE_NAME)

#Training Pipeline related constants

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"


#Data ingestion related constants

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_TRAIN_DATASET_DOWNLOAD_URL_KEY="train_dataset_download_url"
DATA_INGESTION_TEST_DATA_DOWNLOAD_URL_KEY = "test_dataset_download_url"
DATA_INGESTION_INGESTED_DATA_DIR_KEY="ingested_data_dir"
DATA_INGESTION_INGESTED_TRAIN_DATA_DIR_KEY="ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DATA_DIR_KEY="ingested_test_dir" 
DATA_INGESTION_ARTIFACT_DIR_NAME_KEY="data_ingestion"