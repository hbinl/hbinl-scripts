# #################################
# Dot Matrix Printing
# Loh Hao Bin
# #################################

# #################################
# DEFINE
# #################################
on_char = "█"
off_char = " "
newline_input = ","
dimension = 5

dict = {
	"A": [[1,1,1,1,1], [1,0,0,0,1], [1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1] ],
	"B": [[1,1,1,1,1], [1,0,0,0,1], [1,1,1,1,0], [1,0,0,0,1], [1,1,1,1,1]],
	"C": [[1,1,1,1,1], [1,0,0,0,0], [1,0,0,0,0], [1,0,0,0,0], [1,1,1,1,1]],
	" ": [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],
}

# #################################
# Print
# #################################
def dmprint(buffer):
	for line in buffer:
		bound = 0
		for pixel in line:
			bound += 1
			if pixel == 1:
				print(on_char, end="")
			elif pixel == 0:
				print(off_char, end="")
			if bound % dimension == 0:
				print(off_char, end="")
				bound = 0
		print()

def dotmat():
	input_text = list(str(input("Text to print: ")))

	lines = []

	print(input_text)
	buffer = [[]] * dimension

	for c in input_text:
		if c in dict:
			for i in range(dimension):
				buffer[i] = buffer[i] + dict[c][i]

		if c == newline_input:
			lines.append(buffer)
			buffer = [[]] * dimension


	lines.append(buffer)

	#print(lines)
	for line in lines:			
		dmprint(line)
		print()


if __name__ == "__main__":
	dotmat()