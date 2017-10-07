def unique(List,key=None):
	'''
	input:A list and and an optional key
	output:unique elements  of the list based on the key'''
	if  key!=None:
		for i in range(len(List)):
			List[i]=key(List[i])
	d=[]
	for i in List:
		if i not in d:
			d.append(i)
	return d

print(unique(['python','java','Python','Java'],key=lambda s:s.lower()))

