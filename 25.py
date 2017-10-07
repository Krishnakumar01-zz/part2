def map(f,List):
	'''
	input:a function and the list
	output:map implementation '''
	return [f(i) for i in List]
def square(x):
	return x*x
print(map(square,range(5)))
