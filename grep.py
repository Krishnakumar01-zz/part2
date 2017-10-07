import sys
def grep():
	'''
	input:A file and a string
	output:Displays those lines which contains tha string'''
	f=open(sys.argv[1],'r')
	m=sys.argv[2]
	for i in f.readlines():
		if m in i:
			print(i)

grep()
