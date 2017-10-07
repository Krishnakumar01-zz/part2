def sum(List):
	'''
	input:A list of strings or numbers
	output:sum of list  or concatenated string
	'''
	summ=List[0]
	for i in range(1,len(List)):
		summ+=List[i]
	return summ
print(sum(['hello','world'])) 
