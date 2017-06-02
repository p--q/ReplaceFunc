#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
# from replacefunc import replaceFunc
#  
# def newFunc(arg):  # new function
#     print("{} printed by the new function.".format(arg)) 
#      
# # def newFunc2(arg):  # new function2
# #     print("{} printed by the new function2.".format(arg))
#      
# @replaceFunc(("__main__.print", newFunc),)  # old function = new function
# def targetFunc():  # Replace functions in this function
#     print("arg in the taget function")
# 
#      
# targetFunc()  # Call the decorated function
# 
# targetFunc.__wrapped__()  # Call the wrapped function

# 
# from io import StringIO
# from unittest.mock import patch
# 
# def targetFunc():  # Replace functions in this function
#     print("arg in the taget function")
#     len("arg2 in the taget function")
# 
# with patch("sys.stdout", new=StringIO()) as fake_out:  # sys.stdoutをStringIOに置換する。
#     targetFunc()
# 
# print("{} モックからの出力。".format(fake_out.getvalue()))


# from unittest.mock import patch
# def targetFunc():
#     print("ターゲットの関数")
# def newFunc(arg):
# #     print("置換後の関数で{}を出力。".format(arg))
#     lst.append("置換後の関数で{}を出力。".format(arg))
# def replaceFunc():
#     pass   
# if __name__ == "__main__":
#     lst = []
# #     with patch('builtins.print', side_effect = newFunc) as mock_print:
#     with patch('__main__.print', side_effect = newFunc) as mock_print:  
# #     with patch('print', side_effect = newFunc) as mock_print:      
#         targetFunc()
# #         print("test")
# #     targetFunc()
#     print(lst)

# from unittest.mock import patch
# def targetFunc():
#     print("ターゲットの関数")
# def newFunc(arg):
#     print("置換後の関数で{}を出力。".format(arg))
# #     lst.append("置換後の関数で{}を出力。".format(arg))
# def replaceFunc():
# #     lst = []
# #     with patch('builtins.print', side_effect = newFunc) as mock_print:
#     with patch('targetFunc.print', side_effect = newFunc):   
#         targetFunc()
#  
# #     print(lst)   
# if __name__ == "__main__":
# #     lst = []
#      
#     replaceFunc()


from functools import wraps
from unittest.mock import patch

import replacefunc

def targetFunc():
    print("ターゲットの関数")
def replaceFunc(func):
    @wraps(func)
    def wrapper():
        with patch('__main__.print') as print_mock: 
            print_mock.side_effect = replacefunc.newFunc
            func()
    return wrapper
if __name__ == "__main__":
    targetFunc = replaceFunc(targetFunc)
    targetFunc()
   
    

    