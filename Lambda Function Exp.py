# LAMBDA functions are 'nameless', 'anonomous' functions

def num(x):
    return x**3
print(num(10))

num=lambda x:x**3
print(num(10))

def num(x):
    return lambda x:x**3
c=num(3)
print(c(10))

mylist=[1,2,3,4,5,6]
newlist=list(filter(lambda a:(a/3==2),mylist))
print(newlist)

mylist=[1,2,3,4,5,6]
p=list(map(lambda a:(a/3!=2),mylist))
print(p)

from functools import reduce
r=reduce(lambda a,b:a+b,[23,56,43,98,1])
print(r)

s=lambda a: a*a
print(s(4))

d=lambda x,y:3*x+4*y
print(d(4,7))

x=lambda a,b:(a+b)**2
print(x(3,4))
