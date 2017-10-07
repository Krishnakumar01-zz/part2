def read_words(filename):
	return open(filename).read().split()
def word_frequency(words):
	frequency={}
	for w in words:
		frequency[w]=frequency.get(w,0)+1
	return frequency
def main(filename):
	'''input:filename
	   output:returns words in descending order of occurences'''
	frequency=word_frequency(read_words(filename))
	c=frequency.items()
	c.sort(key=lambda x:x[1])
	for i in c[::-1]:
		print(i[0]+' '),

if __name__=='__main__':
	import sys
	main(sys.argv[1])
		
