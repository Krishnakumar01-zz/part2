def invertdict(dicti):
	'''input:a dictionary
	   output:an inverted dictionary'''
	a=dicti.items()
	inv_dicti={}
	for i in a:
		inv_dicti[i[1]]=i[0]
	return inv_dicti

def main():
	print(invertdict({'x':1,'y':2,'z':3}))

if __name__ == '__main__':
	main()
