#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from functools import wraps
from unittest.mock import patch
from io import StringIO

def redirectStdout(func):  
    @wraps(func)
    def wrapper(*args, **kwargs):    
        with patch("sys.stdout", new=StringIO()) as fake_out:
            func(*args, **kwargs)
        print("リダイレクトされた出力{}".format(fake_out.getvalue()))
    return wrapper
    

