"""
FIT1008 Prac 7 Advanced Task
Loh Hao Bin 25461257
@purpose: Infix > RPN
@created 20140915
@modified 20140916
"""

from Task1 import Stack
from Task2 import *
from Task3 import *


def describe_with_precedence(arg):
    """
        @purpose: To identity if the item is an operator, or a higher precedence operator,
                    or an integer, or an invalid string
        @complexity:
            Best & Worst Case: O(1)
        @parameter arg: The string to be tested for type
        @precondition: None
        @postcondition: Return a type code of the string,
    """
    if isnum(arg):
        return 0
    elif arg in ['+','-','==']:
        return 1
    elif arg in ['*','/']:
        return 3
    elif arg.isdigit() == False:
        return 2

def shunting(splitted):
    '''
    @purpose Apply the Djikstra's shunting algorithm to split up an infix expression
            and return a list in RPN
    @parameter  splitted: A splitted expression passed from split()
    @complexity O(n^2) where n is the length of the splitted expression
    @precondition  A splitted expression from split()
    @postcondition  A list containing infix expression in RPN style
    '''
    try:
        #print(splitted)

        if len(splitted) <= 1:
            raise SyntaxError

        #initialise Stack
        stk = Stack(len(splitted))
        rpn = []

        for i in range(len(splitted)):
            type = describe_with_precedence(splitted[i])

            if type == 0:
                #if integer, push into stack
                rpn.append(splitted[i])

            elif type == 1 or type == 3:
                #if encounter operator
                if stk.is_empty() == True:
                    stk.push(splitted[i])
                else:
                    stack_top = stk.peek()

                    if type > describe_with_precedence(stack_top):
                        stk.push(splitted[i])
                    else:
                        while describe_with_precedence(stack_top) >= type and stk.is_empty() == False:
                            rpn.append(str(stk.pop()))
                            stack_top = stk.peek()
                            if stack_top == None:
                                break

                        stk.push(splitted[i])

            elif type == 2:
                #if invalid string, throw error
                print(str(splitted[i]) + ': Invalid String')
                raise SyntaxError

            #print(str(stk))
            #print(rpn)

        while stk.is_empty() == False:
            rpn.append(str(stk.pop()))

        return rpn

    except SyntaxError:
        raise TypeError


def infix_trans():
    """
    @purpose: Accepts and splits an expression, then apply the shunting algorithm
                to convert from infix > RPN
    @complexity: O(n) where n is the length of the expression
    @parameter None
    @precondition A valid infix expression provided
    @postcondition A RPN expression is converted from infix

    """
    try:
        expression = str(input('Please input an infix expression: '))

        if len(expression) > 0:
            splitted = split(expression)
            print('')
            rpn = shunting(splitted)

            expression = str(rpn[0])
            for i in range(1,len(rpn)):
                expression = expression + ' ' + str(rpn[i])
            print('RPN: ' + expression)

            rpn_eval(expression)

        else:
            print('Please input a valid expression.')
    except TypeError:
        print('Please input a valid expression containing integer only.')

def infix_menu():
    """
        @purpose: Display a menu for user input
        @complexity:
        Best & Worst Case: O(1)
    """
    try:
        print('\nInfix -> RPN expression translator.')
        quit = False
        while not quit:
            try:
                print('\n1. Translate an expression')
                print('2. Quit')
                cmd = int(input('Command: '))

                if cmd == 1:
                    infix_trans()
                elif cmd == 2:
                    quit = True
                else:
                    raise ValueError

            except ValueError:
                print('Invalid command.')

    except KeyboardInterrupt:
        print('Program stopped by user.')

if __name__ == "__main__":
    infix_menu()