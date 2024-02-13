# LAMBDA functions are 'nameless', 'anonymous' functions.
# They are still very new to me, but at least we can cheat. lol

# HIGHLIGHT AND COPY CODE, THEN PASTE INTO YOUR PREFERABLE PYTHON APP/IDLE

def num(x):
    return x**3
print(num(10))

num=lambda x:x**3
print(num(10))
'''----------------------------------------------------------------'''
def num(x):
    return lambda x:x**3
c=num(3)
print(c(10))
'''----------------------------------------------------------------'''
mylist=[1,2,3,4,5,6]
newlist=list(filter(lambda a:(a/3==2),mylist))
print(newlist)
'''----------------------------------------------------------------'''
mylist=[1,2,3,4,5,6]
p=list(map(lambda a:(a/3!=2),mylist))
print(p)
'''----------------------------------------------------------------'''
from functools import reduce
r=reduce(lambda a,b:a+b,[23,56,43,98,1])
print(r)
'''----------------------------------------------------------------'''
s=lambda a: a*a
print(s(4))
'''----------------------------------------------------------------'''
d=lambda x,y:3*x+4*y
print(d(4,7))
'''----------------------------------------------------------------'''
x=lambda a,b:(a+b)**2
print(x(3,4))
'''----------------------------------------------------------------'''
x=lambda a:a+10
print(x(5))
'''----------------------------------------------------------------'''
x=lambda a,b:a*b
print(x(5,6))
'''----------------------------------------------------------------'''
x=lambda a,b,c:a+b+c
print(x(5,6,2))
'''----------------------------------------------------------------'''
def myfunc(n):
  return lambda a:a*n

mydoubler=myfunc(2)

print(mydoubler(11))
'''----------------------------------------------------------------'''
def myfunc(n):
  return lambda a:a*n

mytripler=myfunc(3)

print(mytripler(11))
'''----------------------------------------------------------------'''
def myfunc(n):
  return lambda a:a*n

mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
