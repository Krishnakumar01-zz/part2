#making frequency dictionary of characters for each element of list 
def dicti(a):
	'''input:A string
	   output:Frequency dictionary'''
	dicti={}
	for i in a:
		dicti[i]=dicti.get(i,0)+1
	return dicti

def anagram(List):
	'''input:A list
	   output:Anagrams in the list'''
	a=[]
	c=[]
	k=List[:]
	for i in List:
		a.append(dicti(i))                         #appending list of dictionaries to a list
	m=a[:]
	for i in range(len(List)):
		if k!=[]:
			n=List[:]
			a=m[:]
			b=[]
			b.append(List[i])
			for j in range(i+1,len(n)):
				if a[i]==a[j]:
					b.append(n[j])     #appending anagrams to a list
					List.remove(n[j])  #removibg that element from List
					m.remove(a[j])     #removing that element from the list of dictionaries
			c.append(b)
			for i in b:
				k.remove(i)                #for setting exit condition
			
	return c

def main():
	print(anagram(['eat','tea','ate','done','soup','node']))

if __name__=='__main__':
	main()
