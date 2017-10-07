def enumerate(List):
	'''
	input:A list
	output:print index and the corresponding item'''
	return [(i,List[i]) for i in range(len(List))]

for index,item in enumerate(['a','b','c']):
	print(index,item)
