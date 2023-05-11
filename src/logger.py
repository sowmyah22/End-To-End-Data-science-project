# Any executions,errors and changes thats updated will be logged in the log file
import logging,os
from datetime import datetime


logs_path=os.path.join(os.getcwd(),'logs')
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(levelname)s %(message)s",
    level=logging.INFO
)

#if __name__=="__main__":
    #logging.info("Starting logging")