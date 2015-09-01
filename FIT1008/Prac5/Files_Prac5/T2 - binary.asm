#FIT1008 Prac 5 Task 2 - Loh Hao Bin 25461257, Derwinn Ee 25216384

.data
prompt_input: .asciiz "Please input a positive integer: "
prompt_error: .asciiz "Please enter a valid positive integer greater than zero."

.text
main: 	#copy $sp into $fp
	add $fp, $0, $sp
	
	j binary

binary:	
	#print input prompt
	la $a0, prompt_input
	addi $v0, $0, 4
	syscall
	
	addi $v0, $0, 5
	syscall

	#allocate stack for binary()
	addi $sp, $sp, -16
	
	#initialise	
	sw $v0, -4($fp)	#n
	sw $0, -8($fp)	#rev_binary
	sw $0, -12($fp)	#length
	sw $0, -16($fp)
	
	lw $t9, -4($fp)	#load from n
	# if n > 0
	sgt $t0, $t9, $0
	beq $t0, $0, error
	
	lw $t0, -4($fp) 	#t0 = n
	addi $t1, $0, 4		# t1 = 4
	mult $t0, $t1		# 4*n
	mflo $t1		# t1 = 4*n
	addi $a0, $t1, 4	# a0 = 4*n + 4
	addi $v0, $0, 9		#allocate memory
	syscall

	sw $v0, -8($fp)		# store rev_binary address
	lw $t0, -8($fp)		# load rev_binary
	lw $t1, -4($fp)		# load n
	sw $t1, ($t0)		# store n into rev_binary
	
	lw $t2, -16($fp)	# t2 = i = 0
	
	j loop_append
	
loop_append: 
	# append 0s into list
	bge $t2, $t1, next
	
	addi $t4, $0, 4		# t4 = 4
	mult $t4, $t2		# 4 * i
	mflo $t3	
	add $t3, $t3, $t4	# t3 = 4*i + 4
	add $t3, $t3, $t0	# address + 4 + 4*i
	sw $0, ($t3)		# store 0 into t3 address
	
	#lw $a0, ($t3)
	#addi $v0, $0, 1
	#syscall
	
	lw $t2, -16($fp)
	addi $t2, $t2, 1	# increment i
	sw $t2,-16($fp)
	
	j loop_append

next:
	sw $0, -12($fp)		# length = 0	
	j loop_mod
	
loop_mod:
	lw $t0, -4($fp)		# t0 = n
	sgt $t1, $t0, $0	# if n > 0
	beq $t1, $0, next_2
	
	addi $t2, $0, 2		# t2 = 2
	lw $t0, -4($fp)		# t0 = n
	div $t0, $t2		# n / 2
	mfhi $t3		# take n mod 2
	
	lw $t5, -8($fp)		# load address
	lw $t1, -12($fp)	# load length
	addi $t4, $0, 4		# t4 = 4
	mult $t1, $t4		# length * 4
	mflo $t6		# t6 = length * 4
	add $t6, $t4, $t6	# t6 = 4 + length * 4
	add $t5, $t5, $t6	# t5 = address + 4 + length * 4
	sw $t3, ($t5)		# store n mod 2 into ($t5)

	lw $t0, -4($fp)		# t0 = n
	div $t0, $t2
	mfhi $t3		# n % 2
	sub $t0, $t0, $t3	# n = n - n%2
	div $t0, $t2		# n / 2
	mflo $t0		
	sw $t0, -4($fp)		# store n
	
	lw $t1, -12($fp)	# load length
	addi $t1, $t1, 1	# length = length - 1
	sw $t1, -12($fp)	# store length
	
	#lw $a0, ($t5)
	#addi $v0, $0, 1
	#syscall
	
	j loop_mod
	
	
next_2:
	lw $t0, -12($fp)	# load length
	addi $t0, $t0, -1	# length -1
	sw $t0, -12($fp)	# store length

	j loop_print

loop_print:
	lw $t0, -12($fp)
	sge $t1, $t0, $0
	beq $t1, $0, quit
	
	lw $t2, -8($fp)		# load address
	lw $t1, -12($fp)	# load length
	addi $t4, $0, 4		# t4 = 4
	mult $t1, $t4		# length * 4
	mflo $t3		# t3 = length * 4
	add $t3, $t4, $t3	# t3 = 4 + length * 4
	add $t2, $t2, $t3	# t2 = address + 4 + length * 4
	
	lw $a0, ($t2)		# print (address)
	addi $v0, $0, 1
	syscall
	
	lw $t0, -12($fp)	# load length
	addi $t0, $t0, -1	# decrement length
	sw $t0, -12($fp)	# store length
	
	j loop_print

error:	#prints error
	la $a0, prompt_error
	addi $v0, $0, 4
	syscall
	
	j quit
	
quit:	#stopping program
	addi $v0, $0, 10
	syscall
