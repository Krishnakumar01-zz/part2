def filter(f,List):
	'''
	input:a list
	output:Filter implementation'''
	return [x for x in List if f(x)==True]

def even(x):
	return x%2==0

print(filter(even,range(5)))
