def recherche(l,x):
	for i in l:
		if i ==x:
			return True
		else:
			return False
			
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
			
def list1000():
	l=[]
	for i in range(1000):
		l.append(i)
	return l
	
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
    
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
	
def moy(l):
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
		if moy