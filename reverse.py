import sys
def reverse():
	'''
	input:A file  abc.txt
	output:Displays its contents in reverse order''' 
	f=open(sys.argv[1],'r')
	for i in f.readlines()[::-1]:
		print i
	f.close()
reverse()
