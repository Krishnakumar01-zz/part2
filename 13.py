def lensort(List):
	'''
	input:A list
	output:Sorted list of key length'''
	a=[]
	for i in List:
		d=[]
		d.append(i)
		d.append(len(i))
		a.append(d)
	a.sort(key=lambda x:x[1])
	b=[]
	for i in a:
		b.append(i[0])
	return b

print(lensort(['python','perl','java','c','haskell','ruby']))
