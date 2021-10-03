import matplotlib.pyplot as plt
import math as m

def motif(tex,mot):
    if len(mot)>len(tex):
        return False
    else:               
        if tex[0]==mot[0]:
            p=1
            for n in range(1,len(mot)):                
                if tex[n]==mot[n]:
                    p+=1
                else:
                    return motif(tex[1:],mot)
            if p==len(mot):
                    return True
        else:
            return motif(tex[1:],mot)
                   
def fusion(l1,l2):
    l3=[] 
    for i in l1:
        l3.append(i)
    for n in l2:
        l3.append(n)
    return l3

def fusion2(l1,l2):
    for i in l2:
        l1.append(i)

def rotation(l):
    l1=[]
    l1.append(l[len(l)-1])
    l1.append(l[0])
    for i in range(1,len(l)-1):
        l1.append(l[i])
    return l1

def inv(l):
    l1=[]
    for i in range(-1,-len(l)-1,-1):
        l1.append(l[i])
    return l1

def sup(l,r):
    l1=[]
    for i in range(len(l)):
        if i==r:
            continue
        else:
            l1.append(l[i])
    return l1

def sup2(l,r):
    l1=[]
    for i in l:
        if i==r:
            continue
        else:
            l1.append(i)
    return l1

def tri(l):
    for i in range(len(l),0,-1):
        for j in range(i-1):
            if l[j+1]<l[j]:
                a=l[j+1]
                l[j+1]=l[j]
                l[j]=a
    return l

def tir(x,v,alph):
    g=9.81
    y=(-g*x**2)/(2*v**2*m.cos(alph)**2)+m.tan(alph)*x
    return y

def trajectoire(xmax, n, v, alpha):
    lsy=[]
    for i in range(xmax):
        xi=(i*xmax)/n
        lsy.append(tir(xi,v,alpha))
    return lsy

etap=0
def rechdic(l, x):
    global etap
    etap+=1
    mid=int(len(l)/2)
    if x==l[mid]:
    	return True, etap
    elif len(l)==1 and l[0]==x:
    	return True, etap
    elif len(l)==1 and l[0]!=x:
    	return False, etap
    elif x>l[mid]:
    	return rechdic(l[mid:],x)
    else:
    	return rechdic(l[:mid],x)

def interpol (l,x):
    mid=((len(l)-1)*(x-l[0]))/(l[len(l)-1]-l[0])
    if isinstance(mid,int):
        if l[mid]==x:
            return True
        else:
            return False
    elif l[int(mid)]==x:
        return True
    elif l[int(mid)+1]==x:
        return True
    else:
        return False

def s1(n):
    if n==0:
        return -2
    else:
        return (-1/3)*s1(n-1)+1

def somcar(n):
    if n==1:
        return 1
    else:
        return n**2+somcar(n-1)

def puis(x,n):
    if n==0:
        return 1
    elif n>0:
        return x*puis(x,n-1)
    else:
        return puis(1/x,-n)

def puisrap(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return puis(x**2,n/2)
    else:
        return x*puis(x**2,(n-1)/2)

def nbdec(n):
    if n<10:
        return 1
    else:
        return 1+nbdec(n//10)

def somliste(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+somliste(l[1:])

def palindrome(l):
    if len(l)==0 or len(l)==1:
        return  True
    elif l[0]==l[len(l)-1]:
        return palindrome(l[1:-1])
    else:
        return False

print(palindrome(''))


