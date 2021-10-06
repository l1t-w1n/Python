def nbpremsuiv(n):
    for d in range(2,n+1):
        if n%d!=0:
            continue
        elif d==n:
            return n
        else:
            return nbpremsuiv(n+1)

def niemeNbPrem(x):
    n,c=1,0
    while(c<x):
        n+=1
        for i in range(2,n+1):
            if(n%i==0):
                break
        if(i==n):
            c=c+1
    return n

print(niemeNbPrem(3))