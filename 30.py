def parse_csv(a):
	'''input:a file
	   output:parsed list'''
	f=open(a,'r')
	a=f.read().split('\n')
	for i in range(len(a)):
		a[i]=a[i].split(',')
	f.close()
	return a[:-1]

print(parse_csv('a.csv'))
