import sys
f=open(sys.argv[1],'r')
n=int(sys.argv[2])
def wrap(a,n):
	'''
	input:A line in a file and given width
	output:Display lines in that width'''
	if len(a)<n:
		return a
	else:
		print(a[:n])
		return wrap(a[n:],n)
for i in f.readlines():
	print(wrap(i,n))
f.close()		
