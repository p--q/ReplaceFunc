# ReplaceFunc

Replace functions in the function to decorate

(It is better to use <a href="http://docs.python.jp/3.5/library/unittest.mock.html#unittest.mock.patch">unittest.mock.patch() than to use this replaceFunc().)

## Deployment
install replacefunc.py into PYTHONPATH.

## Usage Example


```
from replacefunc import replaceFunc

def newFunc(arg):  # new function
    print("{} printed by the new function.".format(arg)) 
    
def newFunc2(arg):  # new function2
    print("{} printed by the new function2.".format(arg))
    
@replaceFunc(print=newFunc, len=newFunc2)  # old function = new function
def targetFunc():  # Replace functions in this function
    print("arg in the taget function")
    len("arg in the taget function2")
    
targetFunc()  # Call the decorated function
```

targetFunc() is rewritten by replaceFunc() as follows.

```
def targetFunc():  # Replace functions in this function
    #replace functions
    len = newFunc2
    print = newFunc
    print("arg in the taget function")
    len("arg in the taget function2")
```

Adding keyword arguments allows you to output the edited code.

```
targetFunc = replaceFunc(print=newFunc, len=newFunc2)(targetFunc, debug=True)
targetFunc()
```

## Disadvantage

Breakpoint can not be set in the edited code.


## Release Note
v2.0.0 When the value of the keyword argument is a string, the string in the function code of the argument is replaced　with the string.

v2.2.0 Changed to get bytecode and return it. This invalidates ``__wraped__`` in functools.wrap.
