#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from functools import wraps
import inspect   
def indentList(tab, first_line):
    ind = 'if 1:'
    ifs = list()
    first_line = first_line.expandtabs(4)  # 関数定義の先頭行をタブを4つのスペースに置換して取得。
    t = first_line.replace(first_line.lstrip(tab), "").count(tab)  # 行頭のtabの数を取得。     
    for i in range(t):
        ifs.append(tab * i + ind)    
    return ifs, t
def replaceFunc(oldfunc, newfunc):  # func内のoldfuncをnewfuncに置換する。
    def decorate(func):
        tab = "    "  # タブの文字列をスペース4個とする。
        newfunc_src = newfunc if isinstance(newfunc, str) else inspect.getsource(newfunc)
        newfunc_srclines = newfunc_src.splitlines()
        newfunclines, _ = indentList(tab, newfunc_srclines[0])
        newfunclines.extend(newfunc_srclines)
        srclines = inspect.getsource(func).splitlines()  # funcのソースを1行ずつ要素にしたリストを取得。
        for n, line in enumerate(srclines):  # デコレータ式の行番号を取得。
            if '@replaceFunc' in line:
                break        
        else:  # デコレータ式がないとき
            n = -1
        funclines, t = indentList(tab, srclines[n+1])
        srclines.insert(n + 2, tab * (t + 1) + "{} = {}".format(oldfunc.__name__, newfunc.__name__))  # func内に oldfunc = newfunc を挿入。
        funclines.extend(srclines[n+1:])
        funclines.extend(newfunclines)
        src = '\n'.join(funclines)  # funcのソースを再作成。
        temp = dict()  # exec()の仮想モジュールの名前空間を受けとる辞書。
        exec(compile(src,'generated in replaceFunc','exec'), temp, temp)  # srcをコンパイルしてtempに取得。
        @wraps(func)
        def wrapper(*args, **kwargs):
            return temp[func.__name__](*args, **kwargs)  # 作り替えたfuncを返す。
        return wrapper
    return decorate
    