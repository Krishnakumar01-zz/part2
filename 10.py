def unique(List):
	'''
	input:A list
	output:unique elements of the list
	'''
	d=[]
	for i in List:
		if i not in d:
			d.append(i)
	return d

print(unique([1,2,1,3,2,5]))
