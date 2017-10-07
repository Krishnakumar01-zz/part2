import sys
def reverse_lines():
	'''
	input:A file abc.txt
	output:Reverses its each line and diplays it'''
	f=open(sys.argv[1],'r')
	for i in f.readlines():
		print(i[::-1])
	f.close()

reverse_lines()
