import logging
import os
from datetime import datetime

LOG_FILE_DIR = "sales_logs"


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d -- %H-%M-%S')}"
#CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = f"Log_{CURRENT_TIME_STAMP}.log"
#LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_FILE_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)
#LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="%(asctime)s : %(name)s : %(levelname)s : %(message)s",
    level=logging.INFO
)

""" import logging
from datetime import datetime 
import os


LOG_DIR="housing_logs"
CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s -%(message)s',
level=logging.INFO
) """