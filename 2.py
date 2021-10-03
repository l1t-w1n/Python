#def max(li):
#    if len(li)<=1:
#        print('oui')
#    elif li[0]<li[1]:
#        del li[0]
#        max(li)
#    else:
#        print('non')
#
#       
#a=[1, 2, 3, 5, 6]
#max(a)
#import math as m
#while True:
#    a=int(input("enter a"))
#    b=int(input("enter b"))
#    c=int(input("enter c"))
#    if a<=b<=c:
#        break
#
#if a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
#    print("triangle rectangle")
#elif a == b or c == a or b == c:
#    print("triangle isocele")
#else:
#    print("triangle quelconque")
#
#
#
#
#if m.cos(a) + m.cos(b) + m.cos(c) >= 0:
#    print("angle aigu")
#else:
#    print("angle obtus")

#import random as ra
#a=ra.randint(0,99)
#5
#for n in range(6):
#    a+=ra.randint(-3,3)
#    r=int(input("enter r"))
#    if r==a:
#        print("c'est correcte")
#        break
#    elif r>a:
#        print("r est trop grand")
#    else:
#        print("r est trop petit")

#def af_tab(a):
#    for n in range(10):
#        print(f"{a}*{n}={7*n}")
#a=int(input("enter a"))
#af_tab(a=)

#def salut():
#    n=input("enter nom ")
#    p=input("enter prenom ")
#    print(p+" "+n.upper()) 
#
#salut()


c=0
def binome (a,b):
    global c
    c+=1
    if b==0 or b==a:
        return 1
    else:
        return (a/b)*binome(a-1,b-1)



def nbchif (a):
    if a<10:
        return 1
    else: 
        return nbchif(a//10)+1

def somchif (a):
    if a<10:
        return a
    else:
        return a%10+somchif(a//10)

def racnum(a):
    if a<10:
        return a
    else:
        return racnum(somchif(a))

def motif(tex,mot):
    if len(mot)>len(tex):
        return False
    else:
        for n in range(len(mot)):
            if mot[n]==tex[n]:
                

print(motif("nowohu","owo"))

                

