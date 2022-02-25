from itertools import combinations_with_replacement
from ntpath import join
import re
from unittest import result


def concat(*args,**kwargs) -> str:
    r = False 
    k = 'reversed'
    if k in kwargs:
        r = kwargs[k]

    n = len(args)

    if r:
        index_list = range(n-1, -1, -1)
    else:
        index_list = range(0, n, 1)
 
    result = ''
    for i in index_list:
        item = args[i]
        result = result + item
    
    return result 


def inspect(f): 
    def wrap(*args, **kwargs)->str:
        print ('Args:',args)
        print ('Kwargs:',kwargs)
        return f(*args, **kwargs)
    return wrap

x = concat('Hello',' ','world')
print(x)
x = concat('Hello',' ','world', reversed = True)
print(x)


concat = inspect(concat)# @inspect 
x=concat('Hello',' ','world', reversed = True)
print('Retvalue:',x,x)
