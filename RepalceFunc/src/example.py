#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
# from functools import wraps
# from contextlib import redirect_stdout
# from io import StringIO
# def redirectStdout(func):  
#     @wraps(func)
#     def wrapper(*args, **kwargs):  
#         fake_out = StringIO()  
#         with redirect_stdout(fake_out):  # 標準出力をリダイレクト。
#             func(*args, **kwargs)
#         print("リダイレクトされた出力{}".format(fake_out.getvalue()))
#     return wrapper 
# 
# @redirectStdout
# def targetFunc():  # Replace functions in this function
#     print("arg in the taget function")
# 
# targetFunc()  # Call the decorated function


from functools import wraps
from unittest.mock import patch
from io import StringIO
def redirectStdout(func):  
    @wraps(func)
    def wrapper(*args, **kwargs):    
        with patch("sys.stdout", new=StringIO()) as fake_out:  # 標準出力をリダイレクト。
            func(*args, **kwargs)
        print("リダイレクトされた出力{}".format(fake_out.getvalue()))
    return wrapper 

@redirectStdout
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")

targetFunc()  # Call the decorated function