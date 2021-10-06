import math as m
def preminfn(n):
    l=[True for i in range(n+1)]
    l[0]=False
    l[1]=False
    for n in range(2,len(l)):
        for i in range(2,n):
            if n%i==0:
                l[n]=False
    return l
print(preminfn(15))