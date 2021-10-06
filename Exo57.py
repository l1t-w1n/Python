import math as m
def preminfn(n):
    l=[True for i in range(n+1)]
    l[0]=False
    l[1]=False
    for n in range(1,len(l)):
        for i in range(1,int(m.sqrt(n))):
            if n%i==0:
                l[n]=False
    return l
print(preminfn(20))