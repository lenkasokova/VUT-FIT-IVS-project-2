##
# $mainpage IVS Project 2
# $Authors: Zdenek Lapes <xlapes02>
# $Date: 11.3.2021

##
# @file math_lib.py
# @brief Mathematical library with basic functions/operations for calculator
#


import math


# Functions
def is_num(a=0, b=0):
    """is_num Function
    Helps to check if variables are numbers
    @param a
    @param b
    @return Return true if every variable is number, otherwise return false
    """
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
        return False
    else:
        return True


def func_sum(a, b):
    """Sum function
    Add up param a with param b
    @param a float or int
    @param b float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """

    # if param a or param b are not a number
    if is_num(a, b) is False:
        return ValueError

    return round((a + b), 6)


def sub(a, b):
    """Subtract function
    Subtract number b from number a
    @param a float or int
    @param b float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(a, b) is False:
        return ValueError

    return round((a - b), 6)


def multi(a, b):
    """Multiply function
    Multiply number a with number b
    @param a float or int
    @param b float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(a, b) is False:
        return ValueError

    return round((a * b), 6)


def div(a, b):
    """Divide function
    Divide number a and numebr b
    @param a float or int
    @param b float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(a, b) is False:
        return ValueError

    # not define operation
    if b == 0:
        return ValueError

    # ok
    return round((a / b), 6)


def fact(a):
    """Factorial function
    Calculate the factorial from number a
    @param a float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(a) is False or type(a) == float or a < 0:
        return ValueError

    # ok
    factorial = 1
    for i in range(factorial, a + 1):
        factorial = factorial * i

    return round(factorial, 6)


def power(number, exponent=2):
    """Power function
    Exponent is set by defaul to number 2
    @param number float or int
    @param exponent float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(number, exponent) is False:
        return ValueError
    if number == 0 and exponent < 0:
        return ValueError
    elif number == 0 and exponent > 0:
        return 0
    return round(pow(number, exponent), 6)


def root(number, sqrt_root=2):
    """Square Root function
    sqrtRoot is set by default to number 2
    @param number float or int
    @param sqrt_root float or int
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    # if param a or param b are not a number
    if is_num(number, sqrt_root) is False:
        return ValueError

    # not define operation
    if sqrt_root == 0 or (number < 0 and sqrt_root % 2 == 0):
        return ValueError

    # ok
    return round(number**(1/sqrt_root), 6)


def func_sin(number):
    """Sinus Function
    @param number
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    if is_num(number) is False:
        return ValueError
    elif number == 0:
        return 0
    else:
        return round(math.sin(math.radians(number)), 6)


def func_cos(number):
    """Cosinus Function
    @param number
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    if is_num(number) is False:
        return ValueError
    else:
        return round((math.cos(math.radians(number))), 6)


def func_tan(number):
    """Tangens Function
    @param number
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    if is_num(number) is False or number == 90 or number == -270:
        return ValueError
    elif number == 0:
        return 0
    else:
        return round(math.tan(math.radians(number)), 6)


def func_cotan(number):
    """Cotangens Function
    @param number
    @return (int or float): Return value (int or float) if everythink went well, otherwise return ValueError
    """
    if is_num(number) is False or number == 0 or number == 180:
        return ValueError
    else:
        return round(1/math.tan(math.radians(number)), 6)
