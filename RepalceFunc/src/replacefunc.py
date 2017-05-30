#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from functools import wraps
import inspect   
def replaceFunc(oldfunc, newfunc):  # func内のoldfuncをnewfuncに置換する。
    def decorate(func):
        module_name = inspect.getmodulename(__file__)  # newfuncのあるモジュール名を取得。
        srclines = inspect.getsource(func).splitlines()  # funcのソースを1行ずつ要素にしたリストを取得。
        for n, line in enumerate(srclines):  # デコレータ式の行番号を取得。
            if '@replaceFunc' in line:
                break        
        else:  # デコレータ式がないとき
            n = -1
        tab = "    "  # タブの文字列をスペース4個とする。
        defline = srclines[n+1].expandtabs(4)  # 関数定義の先頭行をタブを4つのスペースに置換して取得。
        t = defline.replace(defline.lstrip(tab), "").count(tab)  # 行頭のtabの数を取得。        
        srclines.insert(n+2, tab * (t + 1) + "from {0} import {2}; {1} = {2}".format(module_name, oldfunc.__name__, newfunc.__name__))  # funcのソースを改変する。
        src = '\n'.join(srclines[n+1:])  # funcのソースを再作成。
        ind = ""  # インデントの処理。
        for i in range(t):
            ind += tab * i + 'if 1:\n'
        src = ind + src
        temp = dict()  # exec()の仮想モジュールの名前空間を受けとる辞書。
        exec(compile(src,'virtual_module','exec'), temp, temp)  # srcをコンパイルしてtempに取得。
        @wraps(func)
        def wrapper(*args, **kwargs):
            return temp[func.__name__](*args, **kwargs)  # 作り替えたfuncを返す。
        return wrapper
    return decorate

# def newFunc(arg):  # 置換後の新しい関数。
#     print("置換後の関数で{}を出力。".format(arg)) 
      
# def targetFunc():  # この関数の中の関数を置換する。デコレータ式を使わない時。
#     print("ターゲットの関数")

if __name__ == "__main__":
    def newFunc(arg):  # 置換後の新しい関数。
        print("置換後の関数で{}を出力。".format(arg)) 
    
    @replaceFunc(print, newFunc)  # 引数付きデコレータ。グローバルスコープで使うと2回実行されてしまう。
    def targetFunc():  # この関数の中の関数を置換する。
        print("ターゲットの関数")
    
#     targetFunc = replaceFunc(print, newFunc)(targetFunc)  # デコレータ式を使わない方法。
    
    targetFunc()
    
    
    