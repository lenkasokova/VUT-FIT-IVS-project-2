#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file GUI_mediator.h
@brief Rearrange expressions from input

@author Lenka Šoková (xsokov01)
@bugs No known bugs.
"""


from math_lib import *


def is_number(n):
    """ Check if is n a number function
    Check if n is type of float or int

    :param n any type
    :return: (true or false): Return true if n is a number
                                or false if n is not a number
    """
    if type(n) == int or type(n) == float:
        return True
    return False


def check_str_number(str_number):
    """ Check string number

    Check if a string str_number can be convert to int or float

    :param str_number: string
    :return: true if str_number can be convert tot int or float else return false
    """
    number = ""
    float_number = False

    for i in range(len(str_number)):
        if str_number[i].isdigit():
            number += str_number[i]

        # Check if it is a float number
        elif str_number[i] == '.' and not float_number and number:
            number += str_number[i]
            float_number = True

        else:
            return False

    return True


def replace_string(expression):
    """
    Replace same characters to simplify the calculations
    :param expression: tuple
    :return: simplified expression
    """
    instructions = {'rt': 'r', 'sin': 's', 'cos': 'c', 'cotg': 'g', 'tg': 't', ' ': ''}

    # r : sqrt
    # s : sin
    # c : cos
    # t : tan

    for value, key in instructions.items():
        expression = expression.replace(value, key)

    return expression


def check_expression(expression):
    """
    Check if an expression is written correct
    :param expression: tuple
    :return: true if the expression is written correct else false
    """

    # r : sqrt
    # s : sin
    # c : cos
    # t : tan
    # n : number

    # symbols that can be use BEFORE each symbol
    rules_before = {'+': ('n', ')', '!'),
                    '-': ('n', ')', '!', '', '(', '+', '*', '/'),
                    '*': ('n', ')', '!'),
                    '/': ('n', ')', '!'),
                    '^': ('n', ')'),
                    '!': ('n', ')'),
                    '(': ('+', '-', '*', '/', '^', '', '(', 'r', 's', 'c', 't', 'g'),
                    ')': ('n', ')', '!'),
                    'n': ('+', '-', '*', '/', '^', '', '('),
                    'r': (')', 'n'),
                    's': ('+', '-', '*', '/', '^', '', '('),
                    'c': ('+', '-', '*', '/', '^', '', '('),
                    't': ('+', '-', '*', '/', '^', '', '('),
                    'g': ('+', '-', '*', '/', '^', '', '(')}

    # symbols that can be use AFTER each symbol
    rules_after = {'+': ('n', '(', 's', 'c', 't', 'g', '-'),
                   '-': ('n', '(', 's', 'c', 't', 'g', '-'),
                   '*': ('n', '(', 's', 'c', 't', 'g', '-'),
                   '/': ('n', '(', 's', 'c', 't', 'g', '-'),
                   '^': ('n', '(', 's', 'c', 't', 'g'),
                   '!': ('+', '-', '*', '/', '^', ')', ''),
                   '(': ('n', '(', '!', 's', 'c', 't', 'g', '-'),
                   ')': ('+', '-', '*', '/', '^', '', ')', 'r'),
                   'n': ('+', '-', '*', '/', '^', '', '!', ')', 'r'),
                   'r': '(',
                   's': '(',
                   'c': '(',
                   't': '(',
                   'g': '('}

    # counter of brackets
    cnt_brackets = 0
    simplified_expression = ['n' if is_number(expression[i]) else expression[i] for i in range(len(expression))]

    for i in range(len(simplified_expression)):
        if simplified_expression[i] == '(':
            cnt_brackets += 1

        elif simplified_expression[i] == ')':
            cnt_brackets -= 1

        # if brackets are not used correct
        if cnt_brackets < 0:
            return False

        if (i - 1) >= 0 and simplified_expression[i-1] not in rules_before[simplified_expression[i]]:
            return False

        if (i + 1) < len(simplified_expression) and simplified_expression[i+1] not in rules_after[simplified_expression[i]]:
            return False

        # check first symbol
        elif (i + 1) == len(simplified_expression) and '' not in rules_after[simplified_expression[i]]:
            return False

        #  check last symbol
        elif (i - 1) < 0 and '' not in rules_before[simplified_expression[i]]:
            return False

    if cnt_brackets:
        return False

    return True


def make_list_from_str(input_str):
    """
    Convert input from GUI to tuple
    :param input_str: string
    :return: converted string
    """

    # Operations, which can be used
    operations = ['+', '-', '*', '/', '!', '^', ')', '(', 'r', 's', 'c', 't', 'g']

    i = 0
    str_number = ""
    result = []

    while i < len(input_str):

        if input_str[i] in operations:

            # check number and add to the result
            if str_number and check_str_number(str_number):
                if '.' in str_number:
                    result.append(float(str_number))
                else:
                    result.append(int(str_number))

            elif str_number and not check_str_number(str_number):
                return False

            str_number = ""

            # append operation to the result
            result.append(input_str[i])

        else:
            str_number += input_str[i]

        i += 1

    # Check string number, convert and add to the result
    if str_number:
        if check_str_number(str_number):
            if '.' in str_number:
                result.append(float(str_number))
            else:
                result.append(int(str_number))

        else:
            return False

    return result


def calculate_operation_with_2_operands(symbol, operand1, operand2):
    """
    Calcultate operations that requires 2 operands
    :param symbol: string
    :param operand1: float or int
    :param operand2: float or int
    :return: calculated expression
    """
    if symbol == '*':
        return multi(operand1, operand2)

    elif symbol == '/':
        return div(operand1, operand2)

    elif symbol == '+':
        return func_sum(operand1, operand2)

    elif symbol == '-':
        return sub(operand1, operand2)

    elif symbol == '^':
        return power(operand1, operand2)

    elif symbol == 'r':
        return root(operand2, operand1)


def calculate_operation_with_operand(symbol, operand):
    """
    Calcultate operations that requires 1 operand
    :param symbol: string
    :param operand: float or int
    :return: calculated expression
"""

    if symbol == '!':
        return fact(operand)

    elif symbol == 's':
        return func_sin(operand)

    elif symbol == 'c':
        return func_cos(operand)

    elif symbol == 't':
        return func_tan(operand)

    elif symbol == 'g':
        return func_cotan(operand)


def calculate_expression(expression):
    """
    Calculate the expression based on priority of the instructions
    :param expression: tuple
    :return: (tuple) Calculated expression
    """

    # value: type of instruction
    # key: number of operands
    instructions = {'s': 1, 'c': 1, 't': 1, 'g': 1, 'r': 2, '^': 2, '!': 1, '*': 2, '/': 2, '+': 2, '-': 2}
    before_minus = ('(', '', '+', '/', '-', '*')

    for symbol, count in instructions.items():
        i = 0

        while i < len(expression):
            if (i-1 >= 0 and expression[i] == '-' and expression[i-1] in before_minus) \
                    or i == 0 and expression[i] == '-':
                
                expression[i+1] = -expression[i+1]
                expression.pop(i)
            
            if expression[i] == symbol:

                if count == 1:
                    result = calculate_operation_with_operand(symbol, expression[i-1])

                    if result is ValueError:
                        return False

                    expression[i-1] = result
                    expression.pop(i)

                elif count == 2:
                    result = calculate_operation_with_2_operands(symbol, expression[i-1], expression[i+1])

                    if result is ValueError:
                        return False

                    expression[i-1] = result

                    expression.pop(i)
                    expression.pop(i)
                    i -= 1

            i += 1

    return expression


def priority_brackets(expression):
    """
    Iterate through the expression based on priority of brackets
    :param expression: tuple
    :return: (tuple) calculated expression
    """
    used_bracket = False
    cut_result = []
    cnt_bracket = 0
    i = 0
    new_result = []  # Final result

    while i < len(expression):
        if expression[i] == '(':
            used_bracket = True

            if cnt_bracket:
                cut_result.append('(')

            cnt_bracket += 1

        elif expression[i] == ')':
            cnt_bracket -= 1

            if not cnt_bracket:

                # call priority_brackets function to simplify expression
                new_result += priority_brackets(cut_result)
                cut_result = []
                used_bracket = False

            else:
                cut_result.append(')')

        elif used_bracket:
            cut_result.append(expression[i])

        else:
            new_result.append(expression[i])

        i += 1

    return calculate_expression(new_result)


def calculate(expression):
    """
    Run and start calcate the expression
    :param expression:string
    :return: (int or float) result
    """
    # to simplify the calculation replace some characters
    expression = replace_string(expression)

    # convert string to tuple
    expression = make_list_from_str(expression)

    if expression is False:
        return False

    # Check if is the expression written correct
    if check_expression(expression) is False:
        return False

    # Finally calculate the expression
    expression = priority_brackets(expression)
    if expression is False:
        return False

    # Convert to int or float
    expression = expression[0]
    if int(expression) - float(expression) == 0:
        expression = int(expression)

    return expression
