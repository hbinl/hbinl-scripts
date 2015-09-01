
inp = str("X = alloc(regA, regB, regA, regC, regA) ;\
X = alloc(regA, regB, regA, regC, regB) ;\
X = alloc(regA, regB, regC, regA, regB) ;\
X = alloc(regA, regB, regC, regA, regC) ;\
X = alloc(regA, regC, regA, regB, regA) ;\
X = alloc(regA, regC, regA, regB, regC) ;\
X = alloc(regA, regC, regB, regA, regB) ;\
X = alloc(regA, regC, regB, regA, regC) ;\
X = alloc(regB, regA, regB, regC, regA) ;\
X = alloc(regB, regA, regB, regC, regB) ;\
X = alloc(regB, regA, regC, regB, regA) ;\
X = alloc(regB, regA, regC, regB, regC) ;\
X = alloc(regB, regC, regA, regB, regA) ;\
X = alloc(regB, regC, regA, regB, regC) ;\
X = alloc(regB, regC, regB, regA, regB) ;\
X = alloc(regB, regC, regB, regA, regC) ;\
X = alloc(regC, regA, regB, regC, regA) ;\
X = alloc(regC, regA, regB, regC, regB) ;\
X = alloc(regC, regA, regC, regB, regA) ;\
X = alloc(regC, regA, regC, regB, regC) ;\
X = alloc(regC, regB, regA, regC, regA) ;\
X = alloc(regC, regB, regA, regC, regB) ;\
X = alloc(regC, regB, regC, regA, regB) ;\
X = alloc(regC, regB, regC, regA, regC) ;")
inxx = inp.split(" ;")
inxx = inxx[0:-2]
print(inxx)

for x in inxx:
	y = x[10:-1]
	#print(y)
	inx = y.split(", ")
	#print(inx)
	if inx[0] == inx[1]:
		print("X")
	elif inx[1] == inx[2]:
		print("X")
	elif inx[2] == inx[3]:
		print("X")
	elif inx[3] == inx[4]:
		print("X")
	elif inx[1] == inx[3]:
		print("X")
	else:
		print("EXEC")


