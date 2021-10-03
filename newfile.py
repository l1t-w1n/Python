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
			

print(rechdic([2,5,6,7], 9))
	