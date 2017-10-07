def unique(List,key=None):
	'''
	input:A list
	output:Unique elements of the list using set'''
	if key!=None:
		for i in range(len(List)):
			List[i]=key(List[i])
	return list(set(List))

print(unique(['Python','java','python','Java'],key=lambda s:s.lower()))
