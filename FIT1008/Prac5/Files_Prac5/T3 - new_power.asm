#FIT1008 Prac 5 Task 3 - Loh Hao Bin 25461257, Derwinn Ee 25216384
.data
prompt_input: .asciiz "Please input a positive integer: "
prompt_exponent: .asciiz "Please input positive exponents only."

.text
main: 	#main
	add $fp, $0, $sp	# copy sp into fp
	addi $sp, $0, -8 	#allocate for b & e
	
	#initialise main local variables
	sw $0, -8($fp)		# e = 0
	sw $0, -4($fp)		# b = 0
	
	la $a0, prompt_input
	addi $v0, $0, 4
	syscall
	
	addi $v0, $0, 5
	syscall
	
	sw $v0, -4($fp)
	
	la $a0, prompt_input
	addi $v0, $0, 4
	syscall
	
	addi $v0, $0, 5
	syscall
	
	sw $v0, -8($fp)
	
	# push arguments
	addi $sp, $sp, -8	#allocate stack
	
	lw $t0, -4($fp)		# copy b to arg1
	sw $t0, 4($sp)
	
	lw $t0, -8($fp)		# copy e to arg2
	sw $t0, 0($sp)
	
	jal power
	
	#return from power()
	addi $sp, $sp, 8
	add $a0, $0, $v0
	addi $v0, $0, 1
	syscall
	
	j quit
	
	
power:	#power function
	addi $sp, $sp, -8
	sw $fp, 0($sp)		# save fp 
	sw $ra, 4($sp)		# save ra
	add $fp, $0, $sp	#move fp to sp

	addi $sp, $sp, -12	# allocate sp
	sw $0, -4($fp)		# store rev_binary = 0
	sw $0, -8($fp)		# store result = 0
	sw $0, -12($fp)		# store idx = 0
	
	lw $t0, 8($fp)
	#if e < 0, branch
	slt $t9, $t0, $0
	bne $t9, $0, power_error
	
	addi $sp, $sp, -4
	lw $t0, 8($fp)		# copy e into binary_arg
	sw $t0, 0($sp)		# store into binary_arg
	jal binary		# call binary()
	
	#return
	addi $sp, $sp, 4	# destroy binary_arg
	sw $v0, -4($fp)		# store return value into rev_binary
	addi $t0, $0, 1		#t0 = 1
	sw $t0, -8($fp)		#  result = 1
	lw $t1, -4($fp)		#load rev_binary
	lw $t1, ($t1)		#load length from rev_binary[-1]
	addi $t1, $t1, -1	#length - 1
	sw $t1, -12($fp)	# idx = length[list] - 1
	
	j power_loop
	
power_loop:
	lw $t0, -12($fp)
	slt $t9, $t0, $0
	bne $t9, $0, power_next

	lw $t1, -8($fp)		# t1 = result
	mult $t1, $t1		#result * result
	mflo $t1
	sw $t1, -8($fp)
	
	#lw $a0, -8($fp)
	#addi $v0, $0, 1
	#syscall
	
	lw $t9, -4($fp)		# rev_binary
	lw $t8, -12($fp)	# idx
	addi $t4, $0, 4		# 4
	mult $t8, $t4		# idx * 4
	mflo $t7	
	add $t7, $t7, $t4	# idx*4 + 4
	add $t9, $t9, $t7	# address + idx*4 + 4
	lw $s0, ($t9)		# s0 = rev_binary[idx]
	
	seq $t9, $s0, $0
	bne $t9, $0, power_loop2
	
	# do the inner if part
	lw $s1, -8($fp)		
	lw $s2, 12($fp)
	mult $s1, $s2		#result * base
	mflo $s1
	sw $s1, -8($fp)
	
	j power_loop2
	
power_loop2:
	lw $t6, -12($fp)
	addi $t6, $t6, -1	# idx = idx - 1
	sw $t6, -12($fp)
	
	j power_loop		# looop
	
power_next:
	lw $v0, -8($fp)		#load address into v0 for return
	addi $sp, $sp, 12
	
	lw $fp, 0($sp)
	lw $ra, 4($sp)
	addi $sp, $sp, 8
	jr $ra			# return to main()
	
power_error:
	#prompt for positive exponent
	la $a0, prompt_exponent	
	addi $v0, $0, 4
	syscall
	
	j quit
	

binary: 
	addi $sp, $sp, -8	# allocate stack
	sw $fp, 0($sp)		# store fp
	sw $ra, 4($sp)		# store ra
	add $fp, $0, $sp
	
	addi $sp, $sp, -12
	sw $0, 0($sp)		# i = 0
	sw $0, 4($sp)		# length = 0
	sw $0, 8($sp)		# rev_binary = 0
	
	lw $t0, 8($fp)
	sgt $t9, $t0, $0
	bne $t9, $0, binary_e	#branch if e > 0	
	
	# if e <= 0
	addi $a0, $0, 8
	addi $v0, $0, 9		#allocate memory
	syscall
	
	sw $v0, -4($fp)		# rev_binary = address
	lw $t1, -4($fp)		# load rev_binary
	addi $t2, $0, 1		# t2 = 1
	sw $t2, ($t1)		# store len(rev_binary) = 1 into address+4
	sw $0, 4($t1)		# store 0 into address+4
	lw $v0, -4($fp)		# return $v0
	
	j binary_deallocate
	
binary_e:
	lw $t0, 8($fp)
	addi $t1, $0, 4
	mult $t0, $t1
	mflo $t0
	add $t0, $t0, $t1
	
	add $a0, $0, $t0
	addi $v0, $0, 9
	syscall
	lw $t0, 8($fp)
	sw $t0, ($v0)		#store length
	sw $v0, -4($fp)
	
	j binary_loop1
	
	
binary_loop1:
	lw $t0, -12($fp)	# t0 = i
	lw $t1, 8($fp)		# t1 = e
	lw $t2, -4($fp)		# address
	sge $t9, $t0, $t1
	bne $t9, $0, binary_next
	
	addi $t4, $0, 4		#t4 = 4
	mult $t4, $t0		# 4 * i
	mflo $t3		
	add $t3, $t3, $t4	# 4i + 4
	add $t3, $t3, $t2	# 4i + 4 + address
	sw $0, ($t3) 		# store 0 at address
	
	lw $t0, -12($fp)
	addi $t0, $t0, 1
	sw $t0, -12($fp)	# increment i
	
	j binary_loop1
	
	
binary_next:
	sw $0, -8($fp)		#length = 0
	j binary_loop2
	
binary_loop2:
	lw $t0, 8($fp)
	sle $t9, $t0, $0	# e <= 0
	bne $t9, $0, binary_next2
	
	lw $t1, -8($fp)		# load length

	addi $t4, $0, 4		# t4 = 4
	mult $t1, $t4		# length*4
	mflo $t3
	add $t3, $t3, $t4	# length*4 + 4
	lw $t2, -4($fp)
	add $t3, $t3, $t2	# address + length*4 + 4
	
	lw $t9, 8($fp)		# t9 = e
	addi $t8, $0, 2		# t8 = 2
	div $t9, $t8		# t7 = e % 2
	mfhi $t7
	sw $t7, ($t3)		# store e%2 into list
	
	lw $t9, 8($fp)		# e
	addi $t8, $0, 2		
	div $t9, $t8		# e % 2
	mfhi $t7
	sub $t7, $t9, $t7	# e - e%2
	div $t7, $t8		# (e - e%2) / 2
	mflo $t7
	sw $t7, 8($fp)		#store into e
	
	lw $t6, -8($fp)
	addi $t6, $t6, 1	# length +=  1
	sw $t6, -8($fp)
	
	j binary_loop2
	
binary_next2:
	lw $t0, -4($fp)		#rev_binary
	lw $t1, -8($fp)
	sw $t1, ($t0)		# list[-1] = length

	lw $v0, -4($fp)		# load address into v0 for return
	j binary_deallocate
	

binary_deallocate:
	addi $sp, $sp, 12	# deallocate stack
	lw $fp, 0($sp)		#restore fp
	lw $ra, 4($sp)		# restore ra
	addi $sp, $sp, 8	# deallocate fp and ra
	jr $ra			#return to power()

quit:
	addi $v0, $0, 10
	syscall
	

	
	
	
	
	
