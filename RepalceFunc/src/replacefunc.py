#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
def newFunc(arg):  # new function
    print("{} printed by the new function.".format(arg)) 
    
def newFunc2(arg):  # new function2
    print("{} printed by the new function2.".format(arg))

from functools import wraps
from unittest.mock import patch
def replaceFunc(dic):  # func内のoldfuncをnewfuncに置換する。引数はキー:oldfunc名、値:newfunc関数オブジェクト、の辞書。
    '''
    Replace functions in the function to decorate
    '''
    def decorate(func):
        for key, val in dic.items():
            oldfunc = key
            newfunc = val
        
        
        
        @wraps(func)
        def wrapper(*args, **kwargs):    
            with patch(oldfunc, side_effect=newfunc):  
                func(*args, **kwargs)
        return wrapper
    return decorate
    