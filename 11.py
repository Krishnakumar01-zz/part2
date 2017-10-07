def dups(List):
	'''
	input:A list
	output:Duplicate elements of the list
	'''
	d=[]
	a=[]
	for i in List:
		if i not in d:
			d.append(i)
		else:
			a.append(i)
	return a

print(dups([1,2,1,3,2,5]))
