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

for i in range(1,101):
    print(i**3)
for i in range(10,21):
    print(i**4)
for i in range(0,101,5):
    print(sqrt(i**2))
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


    
                            



    
