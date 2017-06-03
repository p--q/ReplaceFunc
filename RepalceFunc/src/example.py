#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from replacefunc import replaceFunc
import replacefunc

@replaceFunc({"__main__.print": replacefunc.newFunc, "__main__.len": replacefunc.newFunc2})  # key: old function, value: new function
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")
    len("arg in the taget function2")
    
targetFunc()  # Call the decorated function
