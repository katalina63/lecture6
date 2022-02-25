
def fibonacci_1(n,**kwargs)-> int or str:
    num = True
    k = 'num'
    if k in kwargs:
        num = kwargs[k]

    list = [0]
    if n<=1:
        list = [1]
    elif n==2:
        list = [1,1]
    else:
        list = fibonacci_1(n-1,num=False)
        f = list[-1] + list[-2]
        list.append(f)

    
    if num:
        return list[-1]
    else:
        return list
     

    
n = 7
x = fibonacci_1(n)
print (x)


