import sys
def center_align(filename):
	'''
	input:A file
	output:print lines center aligned'''
	f=open(filename,'r')
	max_len=0
	lines=f.readlines()
	for l in lines:
		if len(l)>max_len:
			max_len=len(l)
	for i in lines:
		if len(i)<max_len:
			print((max_len-len(i))/2) * ' ',
		print(i),
	f.close()


def main():
	import sys
	center_align(sys.argv[1])

if __name__=='__main__':
	main()
