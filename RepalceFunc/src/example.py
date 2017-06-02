#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from replacefunc import replaceFunc
import replacefunc

# @replaceFunc({"__main__.print": newFunc, "__main__.len": newFunc2})  # key: old function, value: new function
@replaceFunc({"__main__.print": replacefunc.newFunc})
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")
    len("arg in the taget function2")
    
targetFunc()  # Call the decorated function
