def fact(n):
	'''
	input:A number
	output:Factorial of that number
	'''
	if n==0:
		return 1
	else:
		return product([n,fact(n-1)])

def product(List):
	res=1
	for i in List:
		res=res*i
	return res

print(fact(4))
