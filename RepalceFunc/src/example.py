#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from replacefunc import replaceFunc

def newFunc(arg):  # new function
    print("{} printed by the new function.".format(arg)) 
    
def newFunc2(arg):  # new function2
    print("{} printed by the new function2.".format(arg))
    
@replaceFunc(print=newFunc, len=newFunc2, arg="arg2")  # old function = new function
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")
    len("arg in the taget function2")
    
targetFunc()  # Call the decorated function

def targetFunc2():  # Replace functions in this function
    print("arg in the taget function")
    len("arg in the taget function2")

# If you want to display the edited code, add keyword argument.
targetFunc2 = replaceFunc(print=newFunc)(targetFunc2, debug=True)
targetFunc2()



