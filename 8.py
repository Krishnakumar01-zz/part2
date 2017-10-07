def cumulative_sum(List):
	'''
	input:A list of strings
	output:Cumulative sum of that strings
	'''
	d=[]
	d.append(List[0])
	for i in range(1,len(List)):
		d.append(d[i-1]+List[i])
	return d
print(cumulative_sum(['hello','world','helloworld']))
