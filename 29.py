def array(a,b):
	'''input:the dimensions of the array
           output:multi dimesional array with default value None'''
	m=[]
	for i in range(a):
		n=[]
		for j in range(b):
			n.append(None)
		m.append(n)
	return m
c=array(2,3)
c[0][0]=5
print(c)
