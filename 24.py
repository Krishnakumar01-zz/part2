def zip(a,b):
	'''
	input:two lists
	output:returns zip implementation of lists'''
	return [(a[i],b[i]) for i in range(len(a))]

print(zip([1,2,3],['a','b','c']))
