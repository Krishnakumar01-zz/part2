def mutate(a):
	'''
	input:a string
	output:mutated set of words for tht string'''
	words=[]
	words.append(a)
	for i in range(len(a)):
		words.append(a[0:i]+a[i+1:])
	s='abcdefghijklmnopqrstuvwxyz'
	for i in s:
		words.append(a+i)
		words.append(i+a)
	for i in a:
		for j in s:
			words.append(a.replace(i,j))
	for i in range(len(a)-1):
		m=''
		m=m+a[0:i]+a[i+1]+a[i]+a[i+2:]
		words.append(m)
	return set(words)

words=mutate('hello')
print('hel' in words)
	
