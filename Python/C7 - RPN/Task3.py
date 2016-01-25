"""
FIT1008 Prac 7 Task 3
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: RPN Evaluator
@created 20140913
@modified 20140914
"""

from Task1 import Stack
from Task2 import *

def push_into_stack(splitted):
    """
        @purpose: To evaluate the stack and print the workings for the calculation
        @complexity:
            Best & Worst Case: O(N), where N is the length of the splitted list
        @parameter splitted: Where splitted is a list splitted by split()
        @precondition: A list of splitted operators and operands of an expression
        @postcondition: prints out the calculation and evaluated answer
    """
    try:
        #print(splitted)

        if len(splitted) <= 1:
            raise SyntaxError

        #initialise Stack
        stk = Stack(len(splitted))

        for i in range(len(splitted)):
            #describe type of item in expression
            type = describe(splitted[i])

            if type == 0:
                #if operand, push into stack
                stk.push(splitted[i])

            elif type == 1:
                #if encounter operator, evaluate immediately
                y = stk.pop()
                x = stk.pop()

                if y == 'Stack empty.' or x == 'Stack empty.':
                    print('Warning: Too many operators and not enough operands.')
                    break

                y = int(y)
                x = int(x)
                operator = splitted[i]

                #creating expression
                exp = str(x) + str(operator) + str(y)
                z = int(eval(exp))
                print(str(exp) + ' = ' + str(z))

                #push result into stack
                stk.push(z)

            elif type == 2:
                #if invalid string, throw error
                print(str(splitted[i]) + ': Invalid String')
                raise SyntaxError

        if len(stk) > 1:
            print('Warning: Too many operands and not enough operators.')

    except SyntaxError:
        print('Please input a valid expression with integers and operators only.')

def rpn_eval(expression=''):
    """
        @purpose: To ask for user's input in RPN
        @complexity:
            Best & Worst Case: O(N), where n is length of string the user input
        @parameter: expression: the expression to be evaluated; else if no input provided, it will ask for input
        @precondition: None
        @postcondition: Returns evaluated answer
        """
    if expression == '':
        expression = str(input('Please input an integer expression in RPN: '))
    if len(expression) > 0:
        splitted = split(expression)
        print('')
        push_into_stack(splitted)
    else:
        print('Please input a valid expression.')


def rpn_menu():
    """
        @purpose: Display a menu for user input
        @complexity:
        Best & Worst Case: O(1)
    """
    try:
        print('\nReverse Polish Notation expression evaluator.')
        quit = False
        while not quit:
            try:
                print('\n1. Evaluate an expression')
                print('2. Quit')
                cmd = int(input('Command: '))

                if cmd == 1:
                    rpn_eval()
                elif cmd == 2:
                    quit = True
                else:
                    raise ValueError

            except ValueError:
                print('Invalid command.')

    except KeyboardInterrupt:
        print('Program stopped by user.')


def rpn_tests():
    '''
    @purpose Test cases
    '''
    #testing valid inputs
    rpn_eval('3 5 +')
    rpn_eval('4 3 * 6 2 / +')

    #testing too many operands
    rpn_eval('3 3')

    #testing too many operators
    rpn_eval('4 3 - +')

    rpn_eval('a')

    print('')
    rpn_eval('')

if __name__ == "__main__":
    rpn_tests()
    rpn_menu()