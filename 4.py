def product(List):
	'''
	input:A list
	output:	product of nimbers in list
	'''
	res=1
	for i in List:
		res=res*i
	return res
print(product([1,2,3]))
