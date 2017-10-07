def extsort(List):
	'''
	input:A list
	output:Sorted list based on extension'''
	a=[]
	for i in range(len(List)):
		k=List[i].split('.')
		a.append(k)
	a.sort(key=lambda x:x[1])
	for i in range(len(a)):
		a[i]='.'.join(a[i])
	return a

print(extsort(['a.c','a.py','b.py','bar.txt','foo.txt','x.c']))
