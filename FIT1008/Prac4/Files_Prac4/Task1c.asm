#Loh Hao Bin 25461257 Prac 4 Task 1c
.data
m: .word 0
n: .word 0
a: .word 0
b: .word 0
c: .word 0
prompt: .asciiz "Please input an integer: "
output1: .asciiz "\na = "
output2: .asciiz "\nb = "
output3: .asciiz "\nc = "
msg: .asciiz "Please input only positive integers."

.text
la $a0, prompt			#print prompt
addi $v0, $0, 4
syscall

addi $v0, $0, 5			#input read int
syscall
blt $v0, $0, positive_check
#bltz $v0, positive_check	#check if positive
sw $v0, m			#store read input from $v0 into m

la $a0, prompt			#print prompt
addi $v0, $0, 4
syscall

addi $v0, $0, 5			#input read int
syscall
blt $v0, $0, positive_check
#bltz $v0, positive_check	#check if positive
sw $v0, n			#store read input from $v0 into n

j calc_a1			#start calculating a value

positive_check:
	la $a0, msg		#print output3 if the entered values are not positive
	addi $v0, $0, 4
	syscall
	j quit

calc_a1:
	lw $t1, m		#load m
	mult $t1, $t1		#square m
	mflo $t1

	lw $t2, n		#load n
	mult $t2, $t2		#square n
	mflo $t2
	j calc_c		#use the square value to calculate c first

calc_c:
	add $t0, $t1, $t2	#add m^2 and n^2
	sw $t0, c		#store into c
	j calc_a2		#go back to calculating a

calc_a2:
	sub $t0, $t1, $t2	#subtract m^2 and n^2
	blez $t0, abs		#if $t0 is less than or equal to 0, branch to abs
	j add_to_a		#branch to add_to_a

abs:
	addi $t9, $0, -1	#set up multiplier -1 at $t9
	mult $t0, $t9		#multiply $t0 with -1
	mflo $t0		
	j add_to_a
	
add_to_a:
	sw $t0, a		#store value in a
	j calc_b		#move on to calculate b
	
calc_b:
	lw $t1, m		#get m value
	lw $t2, n		#get n value
	mult $t1, $t2		#multiply m and n
	mflo $t0		
	addi $t9, $0, 2		#setup multiplier 2
	mult $t0, $t9		#multiply by 2
	mflo $t0
	sw $t0, b		#store value in b
	j output
	
output:
	la $a0, output1		#print output1
	addi $v0, $0, 4
	syscall

	lw $a0, a		#load a's content into $a0
	addi $v0, $0, 1		#print integer
	syscall

	la $a0, output2		#print output2
	addi $v0, $0, 4
	syscall

	lw $a0, b		#load a's content into $a0
	addi $v0, $0, 1		#print integer
	syscall

	la $a0, output3		#print output3
	addi $v0, $0, 4
	syscall

	lw $a0, c		#load a's content into $a0
	addi $v0, $0, 1		#print integer
	syscall

	j quit

quit:
	addi $v0, $0, 10 	#exit
	syscall
