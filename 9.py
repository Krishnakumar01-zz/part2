def cumulative_product(List):
	'''
	input:A list
	output:Cumulative product of that list
	'''
	d=[]
	d.append(List[0])
	for i in range(1,len(List)):
		d.append(d[i-1]*List[i])
	return d
print(cumulative_product([1,2,3,4]))
