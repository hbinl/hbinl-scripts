#FIT1008 Prac 5 Task 1 - Loh Hao Bin 25461257, Derwinn Ee 25216384
.data
prompt_size: .asciiz "Please input the size of the list: "
prompt_item: .asciiz "Item: "
prompt_error: .asciiz "Please input a valid length."
space: .asciiz " "

.text
main:	# Copy sp into fp
	addi $fp, $sp, 0

	# Allocate sp for the_list, size and i
	addi $sp, $sp, -12
	
	j reverse
	
reverse:#initialise
	sw $0, -4($fp)	#the_list
	sw $0, -8($fp)	#size
	sw $0, -12($fp)	# i
	
	#ask for size
	la $a0, prompt_size
	addi $v0, $0, 4
	syscall
	
	#accept size input
	addi $v0, $0, 5
	syscall
	sw $v0, -8($fp)
	lw $t0, -8($fp)
	sle $t0, $t0, $0
	bne $t0, $0, error

	
	#allocate memory
	lw $t0, -8($fp)		# load size
	addi $t1, $0, 4
	mult $t0, $t1		# size*4
	mflo $t2
	add $a0, $t1, $t2	# size*4 + 4
	addi $v0, $0, 9		# allocate memory
	syscall
	
	#store address into the_list
	add $t1, $0, $v0	
	sw $t1, -4($fp)		# the_list = address
	sw $t0, ($t1)		# store size into first index

	lw $t0, -8($fp)		#size
	j loop_0
	
loop_0: #Loop 0 to init list with 0s
	lw $t1, -12($fp)	#i
	slt $t2, $t1, $t0
	beq $t2, $0, loop_n
	
	lw $t3, -4($fp)		#t3 = address
	addi $t4, $0, 4		#t4 = 4
	add $t3, $t3, $t4	#t3 = address + 4
	mult $t1, $t4		# i * 4
	mflo $t4		# t4 = i * 4
	add $t3, $t3, $t4	# t3 = t3 + t4 = address + 4 + i*4
	
	sw $0, ($t3)		#initialise list with [0]*size
	
	lw $t1, -12($fp)	#load i
	addi $t1, $t1, 1
	sw $t1, -12($fp)
	
	j loop_0


loop_n:	lw $t0, -8($fp)		#size
	sw $0, -12($fp)		# i = 0
	j loop_1
	
loop_1: #First loop to input items
	lw $t1, -12($fp)	#i
	slt $t2, $t1, $t0
	beq $t2, $0, i_size
	
	la $a0, prompt_item	#print item input prompt
	addi $v0, $0, 4
	syscall
	
	addi $v0, $0, 5		# accept int input
	syscall
	
	lw $t3, -4($fp)		#t3 = address
	addi $t4, $0, 4		#t4 = 4
	add $t3, $t3, $t4	#t3 = address + 4
	mult $t1, $t4		# i * 4
	mflo $t4		# t4 = i * 4
	add $t3, $t3, $t4	# t3 = t3 + t4 = address + 4 + i*4
	
	sw $v0, ($t3)
	
	addi $t1, $t1, 1	#increment i
	sw $t1, -12($fp)
	
	j loop_1
	
	
i_size: #set i to size
	lw $t0, -8($fp)
	addi $t0, $t0, -1
	sw $t0, -12($fp)	# i = size - 1
	j loop_2
	
loop_2:	# second loop to print items
	lw $t1, -12($fp)	#i
	slt $t9, $t1, $0
	bne $t9, $0, quit		# if i < 0
	
	lw $t2, -4($fp)		# t2 = address
	addi $t4, $0, 4
	mult $t1, $t4		# t3 = i * 4
	mflo $t3
	add $t3, $t3, $t4 	# t3 = i*4 + 4
	add $t2, $t2, $t3	# t2 = address + i*4 + 4
	
	lw $a0, ($t2)		#print
	addi $v0, $0, 1
	syscall
	
	la $a0, space		# print space
	addi $v0, $0, 4
	syscall
	
	lw $t1, -12($fp)	# decrement i
	addi $t1, $t1, -1
	sw $t1, -12($fp)
	
	j loop_2
	
error:	#prints error
	la $a0, prompt_error
	addi $v0, $0, 4
	syscall
	
	j quit
	
quit:	#quit
	addi $v0, $0, 10
	syscall
