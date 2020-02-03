# 19.一个数如果恰好等于它的因子之和，这个数就称为“完数”，例如6=1+2+3，编程找出1000以内的所有完数。

from functools import reduce
def sum(a,b):
    return a+b
for i in range(2,1001):
    l = [1]
    for j in range(2,int(i/2+1)):
        if i%j==0:
            l.append(j)
    if i == reduce(sum,l):
        print(i)
        print(l)

