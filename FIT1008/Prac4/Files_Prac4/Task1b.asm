#Loh Hao Bin 25461257 Prac 4 Task 1b
.data
m: .word 0
prompt: .asciiz "Please input an integer: "
output: .asciiz "The absolute value is "

.text
la $a0, prompt	#print prompt
addi $v0, $0, 4 #$v0 = 0 + 4
#li $v0, 4	#$v0 = 4
syscall

addi $v0, $0, 5	#input read int
syscall
sw $v0, m	#store read input from $v0 into m

lw $t0, m	#load m's content into $t0
#ble $t0, $0, abs
sle $t1, $t0, $0
beq $t1,1, abs
#blez $t0, abs	#branch to abs, if $t0's content is <= 0
j next		#branch to next unconditionally

abs: 
	addi $t1,$0,-1	#set $t1 to -1
    	mult $t0,$t1	#multiply $t0 with -1
    	mflo $t0	#move from LO into $t0
    	sw $t0, m	#store $t0's value into m
    	j next	#continue on

next:
la $a0, output	#print output
addi $v0, $0, 4
syscall

lw $a0, m	#load m's content into $a0
addi $v0, $0, 1	#print integer
syscall

addi $v0, $0, 10  #exit
syscall
