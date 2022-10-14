from collections import namedtuple

DataIngestionArtifact =namedtuple("DataIngestionArtifact",["train_dataset_file_path","test_dataset_file_path","is_data_ingested","message"])