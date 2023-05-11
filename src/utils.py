import os,sys
from src.exception import CustomException
import pickle


def save_obj(file_path,obj):
    '''
    This function saves the file as  pickle file
    '''
    try:

        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
     
        with open (file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)






