def isprime(n):
    if n%2==0:
        return n==2
    d=3
    while d*d<=n and n%d !=0:
        d+=2
    return d*d>n

def nnprem(n):
    rep=[]
    k=0
    for i in range(2,n+2):
        for j in range(2,i):
            if i%j==0:
                k+=1
        if k==0:
            rep.append(i)
        else:
            k=0
    return rep

print(nnprem(3))
