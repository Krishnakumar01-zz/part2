def group(List,size):
	'''
	input:A list,size
	output:Group of elemets of give size'''
	a=[]
	for i in range(0,len(List),size):
		d=[]
		for j in range(i,i+size):
			if j<len(List):
				d.append(List[j])
		a.append(d)
	return a

print(group([1,2,3,4,5,6,7,8,9],4))
