.data
ask_month: .asciiz "Please input a month: "
ask_day: .asciiz "Please input a day: "
errormsg: .asciiz "Please input a valid month or date"
month: .word 0
day: .word 0
month_array: .word 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
week_num: .word 0
first_day: .word 2
green: .asciiz "Next Monday you should put out GREEN bin."
yellow: .asciiz "Next Monday you should put out YELLOW bin."
sum: .word 0
week: .word 7
one: .word 1

.text
la $a0, ask_month		#prints prompt for month
addi $v0, $0, 4
syscall

addi $v0, $0, 5			#accept int input
syscall
bgt $v0, 12, error		#check if > 12
blez $v0, error			#check if <= 0
sw $v0, month

la $a0, ask_day			#prints prompt for day
addi $v0, $0, 4		
syscall

addi $v0, $0, 5			#accepts int input
syscall
blez $v0, error			#check if <=0
sw $v0, day			#store it in day

lw $t9, month			#load month
addi $t9, $t9, -1
j day_check

day_check:	
	la $t0, month_array	#load month_array's address
	addi $t1, $0, 4		#$t1 = 4
	mult $t1, $t9		#multiply month-1 by 4
	mflo $t1	
	add $t0, $t0, $t1	#add the multiplier to the array address
	lw $t2, ($t0)		#load the month's days
	
	lw $t3, day		#load day
	bgt $t3, $t2, error	#check if day > the days available for the particular month
	
	j continue

continue:
	sw $v0, day
	addi $t0, $0, 0		#init sum
	lw $t9, month
	addi $t9, $t9, -1
	addi $t8, $0, 0		#init i
	j sum_day
	
sum_day:
	bge $t8, $t9, calculate
	
	la $t7, month_array	#load month_array's address
	addi $t1, $0, 4		#$t1 = 4
	mult $t1, $t8		#multiply i by 4
	mflo $t1	
	add $t7, $t7, $t1	#add the multiplier to the array address
	lw $t2, ($t7)		#load the month's days
	
	add $t0, $t0, $t2	#add the month's day to sum
	
	addi $t8, $t8, 1	#increment i
	j sum_day		#looooop

calculate:
	lw $t1, day		#load day
	add $t0, $t0, $t1	#add day to sum
	addi $t0, $t0, -1	#sum-1
	sw $t0, sum
	
	addi $t1, $0, 7		#$t1 = 7
	lw $t4, first_day	#load first_day
	add $t0, $t0, $t4 	#sum = sum + 2
	div $t0, $t1		#div sum/7
	mfhi $t2		#get remainder
	
	lw $s0, sum
	lw $s1, week
	addi $s2, $0, 1
	div $s3, $s0, $s1
	add $s3, $s3, $s2
	sw $s3, week_num
	
	#lwc1 $f1, sum		#store sum of days into FPR
	#lwc1 $f3, week		#store week into FPR
	#lwc1 $f5, one		#store 1 into FPR
	#div.s $f7, $f1, $f3	#divide in FPR
	#add.s $f7, $f7, $f5	#add 1 in FPR
	#floor.w.s $f7, $f7	#FLOOR in FPR
	#swc1 $f7, week_num	#store result in week_num
	
	lw $t3, week_num	#load week_num
	addi $t3, $t3, 1	#add 2 to week_num
	sw $t3, week_num	#store back into week_num
	
	blt $t2, $t4, increment	#if day_day < first_day, branch
	j modulus
	
increment:
	addi $t3, $t3, 1	# week_num +1 if day_day < first_day
	sw $t3, week_num	# store into week_num
	j modulus
	
modulus:	
	addi $t5, $0, 2		#$t5 = 2
	div $t3, $t5		#$t3 mod 2
	mfhi $t6		# to test for parity
	
	beqz $t6, o_green	#if == 0, green
	la $a0, yellow		#else Yellow
	addi $v0, $0, 4
	syscall

	j quit

o_green:
	la $a0, green
	addi $v0, $0, 4
	syscall
	
	j quit

error:
	la $a0, errormsg	#print invalid input message
	addi $v0, $0, 4
	syscall
	
	j quit
	
quit:
	addi $v0, $0, 10	#quit
	syscall
