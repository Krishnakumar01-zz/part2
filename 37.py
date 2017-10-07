def valuesort(dicti):
	'''input:A dictionary
	   output:sorted list based on key'''
	a=dicti.items()
	a.sort(key=lambda x:x[0])
	b=[]
	for i in a:
		b.append(i[1])
	return b

def main():
	print(valuesort({'x':1,'y':2,'a':3}))

if __name__=='__main__':
		main()
