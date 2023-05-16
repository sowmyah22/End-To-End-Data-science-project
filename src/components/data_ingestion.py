import pandas as pd
import sys,os
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact', 'train_data.csv')
    test_data_path:str=os.path.join('artifact', 'test_data.csv')
    raw_data_path:str=os.path.join('artifact', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        #The 3 variables will get saved in ingestion_config 
    
    def initiate_data_ingestion(self):
        #Will initiate the data ingestion process from the source path specified in the utils.py file
        logging.info("Data ingestion method initiated")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset")

            #if the directory exist dont creat instead save to that directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split is initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.test_data_path,
                self.ingestion_config.test_data_path
            )       
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformations=DataTransformation()
    train_arr,test_arr,_=data_transformations.initiate_data_transformation(train_data,test_data)
            
    modeltrainer=ModelTrainer()
    print(f"Thes best model and its r2 scores are :{modeltrainer.initiate_model_trainer(train_arr,test_arr)}")



# artifact: the output that is created during the training phase. It could be fully trained or checkpoints or file created during the training phase