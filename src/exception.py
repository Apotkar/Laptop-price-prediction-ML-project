import sys
from src.logger import logging


def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error_msg=f'The error is in {0} line no {1} error:{2}'.format(file_name,line_no,error)
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail):
        super().__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
    
if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info('Division by zero')
        raise CustomException(e,sys)

