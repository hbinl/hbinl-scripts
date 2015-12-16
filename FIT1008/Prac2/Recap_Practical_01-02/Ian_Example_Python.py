__author__ = 'Ian Lim'


"""
A sample module
No proper documentation here, see the later sections for proper documentations
:author:    Ian Lim
:since:     20140805
:modified:  20140810
"""


def function_name(parameter_01, parameter_02=True):
    """
    Example function
    :param parameter_01: Need to be added when invoking function_name(). See function_test() below.
    :param parameter_02: If not given when invoking parameter_01() then a default value of True is assigned. See function_test() below.
    :return: Returning two values at once. See function_test() below.
    """
    try:
        print("Parameter_01 = " + str(parameter_01))
        print("Parameter_02 = " + str(parameter_02))
        # python can return more than one variable in a function/ method
        return parameter_01, parameter_02
    except:
        print("Exception goes here.")


def function_test():
    """
    Just a simple function to run the test and act as the main function of the module
    """
    # variables
    print("======================================================")
    variable_01 = 0
    variable_02 = False
    print("variable_01 = " + str(variable_01))
    print("variable_02 = " + str(variable_02))
    # 1 parameter
    variable_01, variable_02 = function_name(99)
    print("variable_01 = " + str(variable_01))
    print("variable_02 = " + str(variable_02))
    # 2 parameter
    variable_01, variable_02 = function_name(-99, False)
    print("variable_01 = " + str(variable_01))
    print("variable_02 = " + str(variable_02))
    print("======================================================")


# To invoke and run function_test as example
# Note that Python is a scripting language. Thus the functions you are invoking need to be before the line which you invoke it. For example function_name() is before the function_test() which invokes it and function_test() is before the line before that invoke it.
function_test()
