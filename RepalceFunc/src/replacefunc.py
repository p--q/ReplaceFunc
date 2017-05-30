#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
from functools import wraps
import inspect   
def indentList(tab, first_line):
    '''
    Hack to deal with indented code
    :param tab: String of one tab
    :type tab: string
    :param first_line: First line of code
    :type first_line: string
    :returns: an list of lines, Number of tabs at the beginning of the line
    :rtype: list, int
    '''
    ind = 'if 1:'
    ifs = list()
    first_line = first_line.expandtabs(4)  # 関数定義の先頭行をタブを4つのスペースに置換して取得。
    t = first_line.replace(first_line.lstrip(tab), "").count(tab)  # 行頭のtabの数を取得。     
    for i in range(t):
        ifs.append(tab * i + ind)    
    return ifs, t
def replaceFunc(**kwargs):  # func内のoldfuncをnewfuncに置換する。引数はキー:oldfunc名、値:newfunc関数オブジェクト、の辞書。newfuncはコードの文字列でも可。 @DontTrace
    '''
    Replace functions in the function to decorate
    '''
    def decorate(func):
        tab = "    "  # タブの文字列をスペース4個とする。
        srclines = inspect.getsource(func).splitlines()  # funcのソースを1行ずつ要素にしたリストを取得。
        for n, line in enumerate(srclines):  # デコレータ式の行番号を取得。
            if '@replaceFunc' in line:
                break        
        else:  # デコレータ式がないとき
            n = -1
        funclines, t = indentList(tab, srclines[n+1])  # インデントへの対応。tはタブの数。       
        newfuncs = list()  # 新しい関数のコードを入れるリスト。   
        tabs = tab * (t + 1)
        exprs = tabs + "#replace functions"  # 挿入する式の文字列。
        for oldfunc, newfunc in kwargs.items():  # 引数の辞書について。
            newfunc_srclines = inspect.getsource(newfunc).splitlines()  # newfuncのコードの行をリストにする。
            newfunclines, _ = indentList(tab, newfunc_srclines[0])  # インデント対応コードを取得。
            newfunclines.extend(newfunc_srclines)  # newfuncのコードのリストを完成。
            newfuncs.extend(newfunclines)
            exprs += "\n" + tabs + "{} = {}".format(oldfunc, newfunc.__name__)
        srclines.insert(n + 2, exprs)  # func内に oldfunc = newfunc を挿入。
        funclines.extend(srclines[n+1:])
        funclines.extend(newfuncs)
        src = '\n'.join(funclines)  # funcのソースを再作成。
        temp = dict()  # exec()の仮想モジュールの名前空間を受けとる辞書。
        exec(compile(src,'generated in replaceFunc','exec'), temp, temp)  # srcをコンパイルしてtempに取得。
        @wraps(func)
        def wrapper(*args, **kwargs):
            return temp[func.__name__](*args, **kwargs)  # 作り替えたfuncを返す。
        return wrapper
    return decorate
    