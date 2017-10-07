import sys
f=open(sys.argv[1],'r')
n=int(sys.argv[2])
def space(i,p):
	'''
	input:A line in a file and the width
	output:The last position where space occurs 
		in the given width'''
	for j in range(p,0,-1):
        	if i[j]==' ':
                	return j
                        break

def wrap(a,n):
	'''
	input:A line in a file and a given width
	output:Displays line in that with without breaking words'''
	if len(a)<n:
                return a
        else:
		m=space(a,n)+1
		print(a[:m])
                return wrap(a[m:],n)

for i in f.readlines():
	print(wrap(i,n))
f.close()
