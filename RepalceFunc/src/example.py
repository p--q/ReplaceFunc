#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from redirectstdout import redirectStdout

@redirectStdout
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")

    
targetFunc()  # Call the decorated function
