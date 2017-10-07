def head(a):
	'''
	input:A file
	output:Displays its first 10 lines'''
	f=open(a,'r')
	print('The head :')
	for i in f.readlines()[:10]:
		print(i)
	f.close()
def tail(a):
	'''
	input:A file
	output:D iaplays its last 10 lines'''
	f=open(a,'r')
	print('The tail:')
	for i in f.readlines()[len(f.readlines())-10:]:
		print(i)
	f.close()

head('abc.txt')
tail('abc.txt')
