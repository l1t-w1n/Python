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

###Exercice 85###
l=[i for i in range(45,56) if i%2==0]
l2=[i for i in range(70) if i%7==0]
l3=[i for i in range(51) if i//10!=2]
l4=[e+str(i) for i in [1,2,3,4] for e in ['a','b','c']]

###Exercice 86###

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