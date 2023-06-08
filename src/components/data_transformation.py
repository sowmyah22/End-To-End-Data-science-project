
import pandas as pd
import sys,os
from dataclasses import dataclass
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj


@dataclass
class DataTransformationConfig:
    preprocessor_file_path=os.path.join("artifact","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def data_transformation(self):
        '''
        - This function provides the transformations that would be performed on the data
        - for Imputing missing values of numerical cols simple imputer by median & 
        - for categorical cols simple imputer by mode is used.
        - Scaling of the data is done by standard scalar.
        - Categorical columns are encoded by Onehot encoding method.
        '''
        try:
            #numerical_columns=['reading_score', 'writing_score'] 
            numerical_columns=['math_score','reading_score','writing_score']
            categorical_columns=['gender', 'race_ethnicity', 'parental_level_of_education', 
                                 'lunch', 'test_preparation_course']
        
            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns:{categorical_columns}")
           
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')), 
                    ('scaling',StandardScaler())
                ]
            )
            
            
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),  
                    ('encoding',OneHotEncoder()),
                    ('scaling',StandardScaler(with_mean=False))
                ]
            )

            logging.info("Column transformer for creating pipeline")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        
        '''
        This function will apply the data transformations to train and test datasets
        '''
        try:
            logging.info("Read the train and test datasets")

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Obtaining the preprocessing object")
            preprocessor_obj=self.data_transformation()
            
            train_df['total_score']=train_df.loc[:,['math_score','reading_score','writing_score']].sum(axis=1)
            test_df['total_score']=test_df.loc[:,['math_score','reading_score','writing_score']].sum(axis=1)

            target_column_name="total_score"
            #target_column_name="math_score"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying the preprocessing object to the training and test data")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

             
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_obj(
                file_path=self.data_transformation_config.preprocessor_file_path,
                obj=preprocessor_obj
            )
            logging.info("saved preprocessing object as pickle file")
            return (
                train_arr, 
                test_arr,
                self.data_transformation_config.preprocessor_file_path
                )

        except Exception as e:
            raise CustomException(e,sys)