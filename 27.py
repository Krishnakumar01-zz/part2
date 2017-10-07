def triplets(n):
	'''
	input:the limit
	output:triplets thst satisfy the condition under the limit'''
	return [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x+y==z]

print(triplets(5))
