#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
def newFunc(arg):  # new function
    print("{} printed by the new function.".format(arg)) 
    
def newFunc2(arg):  # new function2
    print("{} printed by the new function2.".format(arg))

from functools import wraps
from unittest.mock import patch
from contextlib import ExitStack
def replaceFunc(dic):  # func内のoldfuncをnewfuncに置換する。引数はキー:oldfunc名、値:newfunc関数オブジェクト、の辞書。
    '''
    Replace functions in the function to decorate
    '''
    def decorate(func):
        ctx_mgrs = []  # コンテクストマネジャーを入れるリスト。
        for key, val in dic.items():  # key: oldfunc, val: newfunc
            ctx_mgrs.append(patch(key, side_effect=val))  # コンテクストマネジャーをリストに取得。    
 
        @wraps(func)
        def wrapper(*args, **kwargs):    
            with ExitStack() as stack:
                for mgr in ctx_mgrs:
                    stack.enter_context(mgr)  # コンテクストマネジャーのリストを展開。
                func(*args, **kwargs)
        return wrapper
    return decorate
    