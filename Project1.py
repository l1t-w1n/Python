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
    #return mid


print(interpol([2,5,7,12,21,26,33],2))

abcd