def isprime(n):
    if n%2==0:
        return n==2
    d=3
    while d*d<=n and n%d !=0:
        d+=2
    return d*d>n

def nnprem(n):
    rep=[]
    for i in range(1,n):
        if isprime(i):
            rep.append(i)
    return rep


print(nnprem(5))
