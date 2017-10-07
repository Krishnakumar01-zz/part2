def parse_csv(a,b):
	'''input:file and a delimitter
	   output:parsed list'''
	f=open(a,'r')
        a=f.read().split('\n')
        for i in range(len(a)):
        	a[i]=a[i].split(b)
        f.close()
        return a[:-1]
 
print(parse_csv('a.txt','!'))

