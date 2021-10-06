l=[i for i in range(51) if i//10!=2]
l1=[e+str(i) for i in [1,2,3,4] for e in ['a','b','c']]

def estpair(n):
    return n%2==0
def nestpair(n):
    return n%2!=0
def mul7(n):
    return n%7==0
def est20(n):
    return n//10!=2
def cart(x,y):
    return str(x)+y
def moins(n,x):
    return n<x
def sup(n,x):
    return n>x
#a=["a","b","c"] 
#b = [1,2,3,4]
#l=[] 
#for n in range(len(b)):   
#    for i in range(len(a)):
#        l+=(list(map(cart,b, a[i])))
#    b=b[1:]
#print(l)
def pairimp(l):
    l1=list(filter(estpair,l))
    l2=list(filter(nestpair,l))
    return l1+l2

def split(l):
    l1=list(filter(lambda seq: moins(seq, l[0]),l))
    l2=[l[0]]
    l3=list(filter(lambda seq: sup(seq, l[0]),l))
    return l1+l2+l3

ventes={"Vincent":14, "Mickael":19, "Michel":15, "Annie":21}

def ventot(v):
    c=0
    for i in v.keys():
        c+=v[i]
    return c

def plusvent(v):
    c=0
    for i in v.keys():
        if v[i]>c:
            c=v[i]
    for cl,v in v.items():
        if v==c:
            return cl

def freqlet(chaine):
    freq={}
    alph="abcdefghijklmnopqrstuvwxyz"
    for
print(plusvent(ventes))