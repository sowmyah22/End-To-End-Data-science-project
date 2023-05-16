import os,sys
from src.exception import CustomException
import pickle
from sklearn.metrics import r2_score


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
    
def evaluate_models(x_train,y_train,x_test,y_test,models):
    '''
    This function gives the report of the model evaluation
    '''
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]

            model.fit(x_train,y_train)

            y_train_pred=model.predict(x_train)
            y_test_pred=model.predict(x_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
        return report              
    except Exception as e:
        raise CustomException(e,sys)






