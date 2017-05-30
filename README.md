# ReplaceFunc

Replace functions in the function to decorate

'''
from replacefunc import replaceFunc
def newFunc(arg):  # 置換後の新しい関数。
    print("置換後の関数で{}を出力。".format(arg)) 
    
def newFunc2(arg):
    print("置換後の関数2で{}を出力。".format(arg))
    
@replaceFunc(print=newFunc, len=newFunc2)  # 引数付きデコレータ。グローバルスコープで使うと2回実行されてしまう。
def targetFunc():  # この関数の中の関数を置換する。
    print("ターゲットの関数")
    len("ターゲットの関数2")
    
targetFunc()
targetFunc.__wrapped__()
'''
