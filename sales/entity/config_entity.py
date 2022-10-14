from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","test_dataset_download_url",
                                    "ingested_data_dir","ingested_train_dir","ingested_test_dir"])