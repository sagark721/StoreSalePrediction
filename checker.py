from sales.component.data_ingestion import DataIngestion




dataset_download_url= "https://raw.githubusercontent.com/sagark721/Datasets/main/Train.csv"
test_dataset_download_url= "https://raw.githubusercontent.com/sagark721/Datasets/main/Test.csv"

DataIngestion.download_dataset(dataset_download_url=dataset_download_url)