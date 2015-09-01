def gen_combo(size, set):
	gen_combo_rec([], size, set)


def gen_combo_rec(lst, size, set):
	if len(lst) == size:
		custom_print(lst)
	else:
		for char in set:
			lst.append(char)
			lst = gen_combo_rec(lst, size, set)
			lst = lst[:len(lst)-1]
	return lst


def custom_print(lst):
	strr = ""
	for x in lst:
		strr = strr + x + ","
	strr = strr[:len(strr)-1]
	print("[" + strr + "]")


if __name__ == "__main__":
	gen_combo(11,["b","w","u"])