##Exercice 4##
import math as m
a=5
b=4
c=-1
equation = f"{a}*X**2 + {b}*X + {c} = 0"
d= b**2 - 4*a*c
x1= ((-b)+m.sqrt(d))/(2*a)
x2= ((-b)-m.sqrt(d))/(2*a)
print(f"L'équation {equation} admet comme solutions x1={x1} et x2={x2} ")

##Exercice 5##
n=float(input("Nombre d'années d'épargne\n"))
E= 100*0.10**n
print (f"L'épargne au bout de {n} ans est de {E} ")

##Exercice 6##

"""
a=9
b=11
c=a
a=b
b=c
"""


##Exercice 7##
"""

print(EquationDuSecondDegre(a=int(input("valeur de a ? ")),\
b=int(input("valeur de b ? ")),\
c=float(input("valeur de c ? "))))

"""
##Exercice 8##

def calculatrice(a,b,ope):
    if ope == "+":
        return a+b
    elif ope == "-":
        return a-b
    elif ope == "*":
        return a*b
    elif ope == "/":
        return a/b
    
print(calculatrice(a=int(input("valeur de a ? ")),\
b=int(input("valeur de b ? ")),\
ope=input("l'opération ? ")))


##Exercice 9##
import math as m
for i in range(1,101):
    print(i**3)
for i in range(10,21):
    print(i**4)
for i in range(0,101,5):
    print(m.sqrt(i**2))
for i in range(0,11):
    print(2**i)

## Exercice 10

n=int(input("n ?"))
somme=0
for i in range(0,n+1):
    somme=somme+i
print(somme)

##Exercice 11##

n=int(input("n impair ?"))
assert n%2==1, 'bah non'
produit=1
for i in range(1,n+1,2):
    produit=produit*i
print(produit)

##Exercice 12##

for i in range(1,11):
    for j in range(1,11):
        print(i*j)

##Exercice 13##

n=int(input("n?"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print()



##Exercice 14##
from turtle import *
color("blue")
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
forward(100)
left(72)
exitonclick()

from turtle import *
from math import *

##Exercice 15##

def Polygone(long,n):
    for i in range(0,n):
        forward(long/n)
        left(360/n)
#print(Polygone(int(input("la longueur ?")),int(input("le nombre de côté ?"))))

##Exercice 16##

def Spirale(n):
    color('green')
    for i in range(0,n):
        forward(2+i/4)
        left(30-i/12)
#print(Spirale(240))

##Exercice 17##

def graph_fonc():
    setup(1000,1000)
    up()
    for x in range(-200,200):
        y=(1/100)*(x**2)
        goto(x,y)
        down()
#print(graph_fonc())

##Exercice 18##

def Cercle(n):
   up() 
   for i in range(0,n-1):
       
        xi=200*cos((2*i*3.14)/n)
        yi=200*sin((2*i*3.14)/n)
        goto(xi,yi)
        down()
#print(Cercle(100))

##Exercice 20##
import math as m
a=5
b=4
c=-1
equation = f"{a}*X**2 + {b}*X + {c} = 0"
d= b**2 - 4*a*c
if d > 0 :
    x1= ((-b)+m.sqrt(d))/(2*a)
    x2= ((-b)-m.sqrt(d))/(2*a)
    print(f"L'équation {equation} admet deux solutions x1={x1} et x2={x2} ")
elif d == 0 :
    x1=-b/(2*a)
    print(f"L'équation {equation} admet comme unique solution x1={x1}")
else :
    print(f"L'équation n'a pas de solution appartenant à R")

##Exercice 21##
import random as r
a=r.randrange(1,13)
b=r.randrange(1,13)
q=int(input(f"Combien vaut le produit de {a} et {b} ?")) 
if q == a*b :
    print("Bravo")
else :
    print(f"Perdu ! la réponse était {a*b}")

##Exercice 22##
for c in range(10) :    
    for d in range(10):
        for u in range(10):
            n=100*c+10*d+u
            if d%2==0 and c+d+u ==15 and (c+u)%7==0 :
                print(n)

##Exercice 23##
import math as m
print("Choisissez trois nombre a, b et c tel que a<=b<=c.")
a=int(input("Entrez a:\n"))
b=int(input("Entrez b:\n"))
c=int(input("Entrez c:\n"))
if a<=b<=c and (a+b)>c :
    if c**2==(a**2)+(b**2):
        print("Le triangle est réctangle")
    elif a==b==c :
        print("Le triangle est équilatéral")
    elif a==b :
        print("Le triangle est isocèle")
    else :
        print("le triangle est quelconque")

if m.cos(a) + m.cos(b) + m.cos(c) >= 0:
   print("angle aigu")
else:
   print("angle obtus")

##Exercice 24##

import random as ra
a=ra.randint(0,99)
5
for n in range(6):
    r=int(input("enter r"))
    if r==a:
        print("c'est correcte")
        break
    elif r>a:
        print("r est trop grand")
    else:
        print("r est trop petit")

##Exercice 25##
import random as ra
a=ra.randint(0,99)
5
for n in range(6):
    a+=ra.randint(-3,3)
    r=int(input("enter r"))
    if r==a:
        print("c'est correcte")
        break
    elif r>a:
        print("r est trop grand")
    else:
        print("r est trop petit")

##Exercice 26##

def affiche_table_de_7(a):
    for n in range(11):
        print(f"{a}*{n}={7*n}")

##Exercice 27##
def affiche_bonjour() :
    p=input("Quel est votre prénom ? \n")
    print(f"Bonjour {p}")

##Exercice 28## 
def affiche_table(n):
    for i in range(11):
        print(f"{n}*{i}={n*i}")
    
#print(affiche_table(4))

##Exercice 29##
def affiche_salutation(formule):
    p=input("Quel est votre prénom ? \n")
    print (f"{formule} {p}")

#print(affiche_salutation("Coucou"))

##Exercice 30##
def demande_prenom_nom():
    p=input("Quel est votre prénom ? \n")
    n=input("Quel est votre nom ? \n")
    print(f"{p} {n.upper()}") 

##Exercice 31##
def equation_second_deg(a,b,c) :
    equation = f"{a}*X**2 + {b}*X + {c} = 0"
    d= b**2 - 4*a*c
    if d > 0 :
        x1= ((-b)+m.sqrt(d))/(2*a)
        x2= ((-b)-m.sqrt(d))/(2*a)
        print(f"L'équation {equation} admet deux solutions x1={x1} et x2={x2} ")
    elif d == 0 :
        x1=-b/(2*a)
        print(f"L'équation {equation} admet comme unique solution x1={x1}")
    else :
        print(f"L'équation n'a pas de solution appartenant à R")


##Exercice 32 ## 
def multiplication(a,b) :
    n=a
    for i in range(1,b) :
       a+=n
    return a
print(multiplication(5,6))

##Exercice 33 ##
def fact(n):
    if n == 1 :
        return 1
    else :
        return n*fact(n-1)
#print(fact(5))

##Exercice 34##

def IsPrime(n) :
    d = 2
    while n%d != 0 :
        d+=1
    return d==n

##Exercice 35##

def IsPrime2(n) :
    d = 2
    while d*d <= n and n%d != 0 :
        d+=1
    return d*d > n

##Exercice 36##

def IsPrime3(n) :
    if n %2 == 0 :
        return n==2
    d = 3
    while d*d <= n and n%d != 0 :
        d+=2
    return d*d > n

##Exercice 37##

def ListPrime(n):
    rep=[]
    for i in range(1,n):
        if IsPrime3(i):
            rep.append(i)
    return rep


#print(ListPrime(5))


##Exercice 38##
from turtle import *
def Polygone(long,n):
    def main_polygone() :
        forward(long/n)
        left(360/n) 
    for i in range(0,n):
        if n%2 != 0 :
            color('green')
            main_polygone()
        else :
            if i%2 == 0 :
                color('red')
                main_polygone()
            else :
                color('blue')
                main_polygone()          
#print(Polygone(int(input("la longueur ?\n")),int(input("le nombre de côté ?\n"))))

##Exercice 41##

def pgcd(a,b) :
    while a!=b :
        if a>b :
            a=a-b
        else :
            b=b-a
    return a 

##Exercice 42##
def moyenne() :
    a=b=n=m=0

    while a >= 0 :
        a = int(input(f"Entrez un nombre :\n"))
        b+=a
        n+=1
        if b==a :
            print(b)
        else :  
            m=b/n
            print(m)
#print(moyenne())

##Exercice 43##

       
    
    











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
                            



    
