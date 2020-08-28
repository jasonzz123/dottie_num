# Dottie number.  cos x = x
import math

e=0.0000001
N =0

def dottie(x):
    next = math.cos(x)
    if abs(next-x) < e:
       return x
    else:
       global N #!!!
       N +=1
       return dottie(next)

init=0.5

re = dottie(init)
print('Initial number is:%f' % init)
print('Dottie Number is:%f' % re)
print('Iter count is:%d'%N)

