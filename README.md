# ReplaceFunc

Replace functions in the function to decorate

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

targetFunc.__wrapped__()  # Call the wrapped function
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

## Release Note
v2.0.0 When the value of the keyword argument is a string, the string in the function code of the argument is replaced　with the string.
