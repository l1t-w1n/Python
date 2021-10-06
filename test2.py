def isprime(n):
    if n%2==0:
        return n==2
    d=3
    while d*d<=n and n%d !=0:
        d+=2
    return d*d>n


l=[i+2 for i in range(45,56)]
print(list(filter(isprime, l)))

