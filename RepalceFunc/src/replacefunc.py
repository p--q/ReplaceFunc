#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-


def newFunc(arg):  # 置換後の新しい関数。
    print("置換後の関数で{}を出力。".format(arg))
    
    
from functools import wraps
import inspect   
def replaceFunc(oldfunc, newfunc):  # func内のoldfuncをnewfuncに置換する。
    def decorate(func):
        print("実行")
        @wraps(func)
        def wrapper(*args, **kwargs):
            module_name = inspect.getmodulename(__file__)  # newfuncのあるモジュール名を取得。
            srclines = inspect.getsource(func).splitlines()  # funcのソースを1行ずつ要素にしたリストを取得。
            for n, line in enumerate(srclines):  # @デコレータ式がある行番号を取得。
                if '@replaceFunc' in line:
                    break 
            else:
                n = -1  # デコレータ式がないとき      
            srclines.insert(n+2,"""
    from {0} import {2}
    {1} = {2}
        """.format(module_name, oldfunc.__name__, newfunc.__name__))  # funcのソースを改変する。
            src = '\n'.join(srclines[n+1:])  # @デコレータ式を除いてfuncのソースを再作成。
            print(src)
            temp = dict()  # exec()の仮想モジュールの名前空間を受けとる辞書。
            exec(compile(src,'virtual_module','exec'), temp, temp)  # srcをコンパイルしてtempに取得。    
            return temp[func.__name__](*args, **kwargs)  # 作り替えたfuncを返す。
        return wrapper
    return decorate

@replaceFunc(print, newFunc)
def targetFunc():  # この関数の中の関数を置換する。
    print("ターゲットの関数")


if __name__ == "__main__":
#     targetFunc = replaceFunc(print, newFunc)(targetFunc)
    targetFunc()
    targetFunc.__wrapped__()
    
    
    