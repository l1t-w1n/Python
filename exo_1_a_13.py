from math import sqrt

### EXO PYTHON REMISE A NIVEAU

### exo 1

print(60*60*24*365*100)
print(123456789**6)
"761"

### exo 2

"""

False
True
True
True
False
False
False
True
False
True

"""

### exo 3

"""

True
False
True
True

"""

### exo 4

def EquationDuSecondDegre(a,b,c):
    delta= (b**2)-4*a*c
    print("le discrimitant est",delta,)
    if delta > 0:
        solution1=(-b+sqrt(delta))/(2*a)
        solution2=(-b-sqrt(delta))/(2*a)
        print("les solutions sont",solution1,"et",solution2,) 
    elif delta == 0:
        solution=-b/(2*a)
        print("la solution est",solution,)
    else :
        return print("pas de solution")
### exo 5

def Epargne(somme):
    for i in range(3):
        somme=somme*1.10
        print(somme)

### exo 6

"""
a=9
b=11
c=a
a=b
b=c
"""


### exo 7
"""

print(EquationDuSecondDegre(a=int(input("valeur de a ? ")),\
b=int(input("valeur de b ? ")),\
c=float(input("valeur de c ? "))))

"""
### exo 8

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


### exo 9

for i in range(1,101):
    print(i**3)
for i in range(10,21):
    print(i**4)
for i in range(0,101,5):
    print(sqrt(i**2))
for i in range(0,11):
    print(2**i)

### exo 10

n=int(input("n ?"))
somme=0
for i in range(0,n+1):
    somme=somme+i
print(somme)

### exo 11

n=int(input("n impair ?"))
assert n%2==1, 'bah non'
produit=1
for i in range(1,n+1,2):
    produit=produit*i
print(produit)

### exo 12

for i in range(1,11):
    for j in range(1,11):
        print(i*j)

### exo 13

n=int(input("n?"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end=" ")
    print()


    
                            



    
