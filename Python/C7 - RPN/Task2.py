"""
FIT1008 Prac 7 Task 2
Loh Hao Bin 25461257, Tan Wen Jie 25839063
@purpose: String interpreter
@created 20140913
@modified 20140914
"""

from Task1 import Stack

def isnum(arg):
    """
        @purpose: To check if the item is a number
        @complexity:
        Best & Worst Case: O(1)
        @parameter arg: The integer to be tested for integerness
        @precondition: None
        @postcondition: True/False
    """
    try:
        int(arg)
        return True

    except ValueError:
        return False
    except TypeError:
        return False

def print_describe(arg,code):
    """
        @purpose: To name the item if it is an operator, or an integer, or an invalid string
        @complexity:
            Best & Worst Case: O(1)
        @parameter arg: The string to be tested for type
                    code: The type code returned from describe()
        @precondition: A type code returned from describe()
        @postcondition: Print the type of the string
    """
    if code == 0:
        print(str(arg) + ' Integer')
    elif code == 1:
        print(str(arg) + ' Operator')
    elif code == 2:
        print(str(arg) + ' Invalid String')

def describe(arg):
    """
        @purpose: To identity if the item is an operator, or an integer, or an invalid string
        @complexity:
            Best & Worst Case: O(1)
        @parameter arg: The string to be tested for type
        @precondition: None
        @postcondition: Return a type code of the string
    """
    if isnum(arg):
        return 0
    elif arg in ['+','-','*','/','==']:
        return 1
    elif arg.isdigit() == False:
        return 2


def str_desc(list):
    """
        @purpose: Iterate through the list to describe each of them
        @complexity:
        Best & Worst Case: O(N), where n is the length of "stk"
        @parameter  list: consist of the splitted items from split()
        @precondition: A list of splitted items returned by split()
        @postcondition: Description of each item
    """
    try:

        for j in range(len(list)):
            x = list[j]
            c = describe(x)
            print_describe(x, c)
    except:
        pass

def split(inp):
    """
    @purpose: To separate items that are delimited by space into a list
    @complexity:
    Best & Worst Case: O(N), where n is the size of the string
    @parameter inp: where inp is the string that the user input
    @precondition: A string to be splitted
    @postcondition: returns a list with items from the string
    """
    try:
        inp = str(inp)
        list = []
        min = 0
        max = 0
        while max < len(inp):
            if inp[max] == ' ':
                list.append(inp[min:max])
                min = max+1
            max += 1
        list.append(inp[min:max])
        #print(stk.the_array)
        return list
    except AttributeError:
        print('x')
    except AssertionError:
        print("Please insert a valid expression.")


def prompt(inp=''):
    """
    @purpose: To ask for user input
    @complexity:
    Best & Worst Case: O(N), where n is the size of the string
    @parameter inp (optional): where inp is the string that the user input, else if no input provided,
                the function will ask for input.
    @precondition: None
    @postcondition: Prints the description of each item in the expression
    """
    if inp == '':
        inp = input("Character strings separated by spaces:")

    splitted = split(inp)
    print(splitted)
    str_desc(splitted)

def test_function():
    '''
    @purpose Test Cases
    '''
    prompt('12 3 + -8ha -98')
    prompt(' ')
    prompt(90)
    prompt('%')
    prompt()

if __name__ == "__main__":
    test_function()

