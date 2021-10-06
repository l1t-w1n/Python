import math as m

###Exercice 56###
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

###Exercice 57###
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

###Exercice 58###
def fusion(l1,l2):
    l3=[] 
    for i in l1:
        l3.append(i)
    for n in l2:
        l3.append(n)
    return l3

###Exercice 59###
def fusion2(l1,l2):
    for i in l2:
        l1.append(i)
    return l1

###Exercice 60###
def rotation(l):
    l1=[]
    l1.append(l[len(l)-1])
    l1.append(l[0])
    for i in range(1,len(l)-1):
        l1.append(l[i])
    return l1

###Exercice 61###
def inv(l):
    l1=[]
    for i in range(-1,-len(l)-1,-1):
        l1.append(l[i])
    return l1

###Exercice 62###
def sup(l,r):
    l1=[]
    for i in range(len(l)):
        if i==r:
            continue
        else:
            l1.append(l[i])
    return l1

###Exercice 63###
def sup2(l,r):
    l1=[]
    for i in l:
        if i==r:
            continue
        else:
            l1.append(i)
    return l1

###Exercice 64###
def tri(l):
    for i in range(len(l),0,-1):
        for j in range(i-1):
            if l[j+1]<l[j]:
                a=l[j+1]
                l[j+1]=l[j]
                l[j]=a
    return l

###Exercice 65###
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


###Exercice 66###
def recherche(l,x):
	for i in l:
		if i ==x:
			return True
		else:
			return False

###Exercice 68###

###Exercice 70###
def rechdic(l, x):
    mid=int(len(l)/2)
    if x==l[mid]:
    	return True
    elif len(l)==1 and l[0]==x:
    	return True
    elif len(l)==1 and l[0]!=x:
    	return False
    elif x>l[mid]:
    	return rechdic(l[mid:],x)
    else:
    	return rechdic(l[:mid],x)

###Exercice 72###
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

###Exercice 75###
def s1(n):
    if n==0:
        return -2
    elif n>0:
        return (-1/3)*s1(n-1)+1

###Exercice 76###
def somcar(n):
    if n==1:
        return 1
    else:
        return n**2+somcar(n-1)

###Exercice 77###
def puis(x,n):
    if n==0:
        return 1
    elif n>0:
        return x*puis(x,n-1)
    else:
        return puis(1/x,-n)

###Exercice 78###
def puisrap(x,n):
    if n==0:
        return 1
    elif n%2==0:
        return puis(x**2,n/2)
    else:
        return x*puis(x**2,(n-1)/2)

###Exercice 80###
def nbdec(n):
    if n<10:
        return 1
    else:
        return 1+nbdec(n//10)

###Exercice 81###
def somliste(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+somliste(l[1:])

###Exercice 82###
def palindrome(l):
    if len(l)==0 or len(l)==1:
        return  True
    elif l[0]==l[len(l)-1]:
        return palindrome(l[1:-1])
    else:
        return False

###Exercice 83###

###Exercice 84###
l=list(filter(estPremier3, [i for i in range(1001)]))

###Exercice 85###
l=[i for i in range(45,56) if i%2==0]
l2=[i for i in range(70) if i%7==0]
l3=[i for i in range(51) if i//10!=2]
l4=[e+str(i) for i in [1,2,3,4] for e in ['a','b','c']]

###Exercice 86###
#l1# 
def imp(n):
    return n%2!=0
l=list(filter(imp, [i for i in range(30)]))
#l2# 
def mul7(n):
    return n%7==0
l=list(filter(mul7, [i for i in range(70)]))
#l3#  
def vingtaine(n):
    return n//10==2
l=list(filter(not vingtaine, [i for i in range (51)]))    
#l4#
def cart(x,y):
    return str(x)+y
a=["a","b","c"] 
b = [1,2,3,4]
l=[] 
for n in range(len(b)):   
    for i in range(len(a)):
        l+=(list(map(cart,b, a[i])))
    b=b[1:]

###Exercice 87###
def estpair(n):
    return n%2==0
def nestpair(n):
    return n%2!=0
def pairimp(l):
    l1=list(filter(estpair,l))
    l2=list(filter(nestpair,l))
    return l1+l2

###Exercice 88###
def moins(n,x):
    return n<x
def sup(n,x):
    return n>x
def split(l):
    l1=list(filter(lambda seq: moins(seq, l[0]),l))
    l2=[l[0]]
    l3=list(filter(lambda seq: sup(seq, l[0]),l))
    return l1+l2+l3

###Exercice 89###

###Exercice 90###
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

###Exercice 91###
def nOcc(chaine):
	nbOcc={}
	alph="abcdefghijklmnopqrstuvwxyz"
	for i in alph:
		cpt=0
		for n in chaine:
			if i==n:
				cpt+=1
		if cpt!=0:
			nbOcc[i]=cpt
	return nbOcc

###Exercice 92###
def moy(l):
	if len(l)==0:
		return 0
	else:
		a=0
		for i in l:
			a+=i
	return a/len(l)
def bestmoy(dic):
	m=0
	for val in dic.keys():
		if moy(dic[val])>m:
			m=moy(dic[val])
	for cl, val in dic.items():
		if m==moy(dic[cl]):
			return cl

###Exercice 93###
def fusion(d1,d2):
	d3={}
	for k1,v1 in d1.items():
		for k2,v2 in d2.items():
			if k1==k2:
				d3[k1]=v1+v2
			elif k1 not in d3:
				d3[k1]=v1
			elif k2 not in d3:
				d3[k2]=v2
	return d3

###Exercice 94###
def pers(dic):
	for k1,v1 in dic.items():
		nom=[]
		for k2,v2 in v1.items():
			nom.append(v2)
		print(f"{nom[0]} {nom[1]} a {nom[2]} ans")

###Exercice 95,96###
file1=open("1.txt", "r")
l=file1.readlines()
for i in range(len(l)):
	print(f"{i+1} {l[i]}")
file1.close()