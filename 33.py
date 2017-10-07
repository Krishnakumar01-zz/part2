def mutate(a):
	'''input:A string
	   output:Mutated list of words'''
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
       	return words

def nearly_equal(a,b):
	return a in mutate(b)

print(nearly_equal('perl','pearl'))
