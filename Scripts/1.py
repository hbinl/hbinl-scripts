def m(list):
	list2 = []
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			if (list[i] == list[j] and list[j] not in list2):
				list2.append(list[i]) 
	return list2



x = ["a", "b", "c", "d", "b", "b", "c", "b", "e", "c", "e", "f", "f", "d", "e"]
print(m(x))