import math as m
def preminfn(n):
    l=[True for i in range(n+1)]
    l[0]=False
    l[1]=False    
    for n in range(2,len(l)):
        d=2
        while d<=m.sqrt(n) and n%d!=0:
            d+=1
        l[n]=d*d>n
    return l
print(preminfn(11))