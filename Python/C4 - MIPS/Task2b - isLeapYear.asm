#Loh Hao Bin 25461257 Prac 4 Task 2
.data
year: .word 0
msg_leap: .asciiz "Is a leap year"
msg_notleap: .asciiz "Is not a leap year"
msg_error: .asciiz "Please input a valid Gregorian calendar year after 1582"
prompt: .asciiz "Please enter a year: "

.text
la $a0, prompt			#print initial prompt
addi $v0, $0, 4
syscall

addi $v0, $0, 5			#read int
syscall

sw $v0, year			#store int into year
lw $t1, year
addi $t0, $0, 1582		#set up 1582 for comparison
bge $t0, $t1, error		#branch if $t0 (1582) > $t1
j leap_1

leap_1:				#calculate all conditions and perform logical check
	addi $t7, $0, 400
	div $t1, $t7
	mfhi $t2		#div by 400

	addi $t8, $0, 4
	div $t1, $t8	
	mfhi $t3		#div by 4

	addi $t9, $0, 100
	div $t1, $t9
	mfhi $t4		#div by 100

	beqz $t2, is_leap	#if div by 400
	b leap_2

leap_2:
	beqz $t3, leap_3	#if div by 4
	b not_leap

leap_3:
	bnez $t4, is_leap	#if not div by 100
	b not_leap

is_leap:			#print if leap
	la $a0, msg_leap
	addi $v0, $0, 4
	syscall
	j exit

not_leap:			#print if not leap
	la $a0, msg_notleap
	addi $v0, $0, 4
	syscall
	j exit

error:				#print error message
	la $a0, msg_error
	addi $v0, $0, 4
	syscall
	j exit

exit:
	addi $v0, $0, 10	#exit
	syscall
