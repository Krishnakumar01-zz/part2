def max(List):
	'''
	input:A list
	output:Maximum of that list
	'''
	max=List[0]
	for i in range(1,len(List)):
		if List[i]>max:
			max=List[i]
	return max
def min(List):
	'''
	input:A list
	output:Minimum of that list
	'''
	min=List[0]
	for i in range(1,len(List)):
		if List[i]<min:
			min=List[i]
	return min

print(max(['ab','ac','bd']))
print(min(['ab','ac','bd']))
