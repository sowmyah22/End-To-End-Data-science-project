import sys,logging
from src import logger

def error_message_detail(error,error_detail:sys):
    _,_,exec_tb=error_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured while executing script name [{0}],line number [{1}],error_message [{2}]".format(
        file_name,exec_tb.tb_lineno,str(error))
    return error_message

# A self constructor, however, is not a commonly used term. 
# It might refer to the constructor method of a class that takes a reference to the object itself as an argument. 
# In Python, this reference is usually called "self".

# inheriting parent exception class 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info(e)
        raise CustomException(e,sys)