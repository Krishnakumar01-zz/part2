def reverse(List):
	'''
	input:A list
	output:Reverse of that list
	'''
	i=len(List)-1
	d=[]
	while i>=0:
		d.append(List[i])
		i-=1
	return d

print((reverse([1,2,3,4])))
