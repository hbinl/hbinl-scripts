#Loh Hao Bin 25461257 Prac 4 Task 3
.data
size: .word 0	#size of the list
the_list: .word 0	#address of the list
prompt: .asciiz "Please input an item: "
askforlength: .asciiz "Please input the size of the list: "
errormsg: .asciiz "Please input a valid size"
sum: .word 0
summsg: .asciiz "\nThe sum until negative is: "

.text
la $a0, askforlength	
addi $v0, $0, 4			#prints ask for length
syscall

addi $v0, $0, 5
syscall				#accept input integer	
bltz $v0, error			#if input <= 0, error

sw $v0, size			#save size
	
lw $t0, size 			#load size into $t0

addi $t1, $0, 4  		#$t1 = 4
mult $t1, $t0			#multiply length of list with 4
mflo $t2			#move from LO
add $a0, $t2, $t1		#$a0 = 4*length + 4
addi $v0, $0, 9			#9 = allocate memory
syscall

sw $v0, the_list		#save address of the_list
sw $t0, ($v0)			#store length into first index of the_list

addi $t0, $0, 0			#initialise i
j loop			

loop:	
	lw $t1, size		#load size into $t1
	bge $t0, $t1, endloop	#if i >= size
	
	la $a0, prompt		#prompt
	addi $v0, $0, 4
	syscall
	
	addi $v0, $0, 5		#accept int input
	syscall
	
	lw $t2, the_list	#load address of the_list
	addi $t3, $0, 4		#$t3 = 4
	mult $t3, $t0		# i*4
	mflo $t4
	add $t4, $t4, $t3 	#$t4 = $t4 (i*4) + 4
	add $t4, $t4, $t2 	#$t4 = (i*4+4) + address of the_list
	sw $v0, ($t4)		#store $v0 (input) into location stored in $t4
	
	addi $t0, $t0, 1	#increment i
	
	j loop			#loooooop

	
endloop:
	addi $t0, $0, 0 	#initialise $t0
	j print
	
print:
	lw $t1, the_list	#load address of the_list
	lw $t2, ($t1) 		#load size of the_list
	
	bge $t0, $t2, sum_1
	
	addi $t3, $0, 4		#$t3 = 4
	mult $t3, $t0		#i*4
	mflo $t4
	add $t4, $t4, $t3 	#$t4 = i*4+4
	add $t4, $t4, $t1	#$t4 = (i*4+4) + address of the _list
	
	lw $a0, ($t4)		#load content of address pointed to in $t4
	addi $v0, $0, 1		#1 = print integer
	syscall
	addi $a0, $0, 32	#print space
	addi $v0, $0, 11	#11 = print char
	syscall
	addi $t0, $t0, 1	#i=i+1
	
	j print			#loooooop

sum_1:
	addi $t0, $0, 0		#initialise i
	addi $t6, $0, 0		#initialise sum
	j sum_2
	
sum_2: 
	lw $t1, the_list	#load the_list address
	lw $t2, ($t1)		#load length of list
	
	bge $t0, $t2, printsum	#if i >= length
	
	addi $t3, $0, 4		#$t3 = 4
	mult $t3, $t0		# i*4
	mflo $t4		
	add $t4, $t4, $t3	#$t4 = (i*4)+4
	add $t4, $t4, $t1	#$t4 = $t4 + address of the_list
		
	lw $t5, ($t4)		#load content of $t4 to $t5
	bltz $t5, printsum	#ends if $t5 is < 0
	add $t6, $t6, $t5 	#sums up

	addi $t0, $t0, 1	#i=i+1
	j sum_2			#loooooop

printsum:
	sw $t6, sum		#store sum in sum
	
	la $a0, summsg		#print The sum is:
	addi $v0, $0, 4		#4 = print string
	syscall
			
	lw $a0, sum		#load sum into $a0
	addi $v0, $0, 1		#1 = print integer
	syscall	
	j quit			#doneeeee

error: 
	la $a0, errormsg	#print error message
	addi $v0, $0, 4
	syscall
	j quit	
		
quit:	
	addi $v0, $0, 10	#quit
	syscall
