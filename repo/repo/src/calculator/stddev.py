"""
@file stddev.py
@brief Script to profile math library

@author Lenka Šoková (xsokov01)
@bugs No known bugs
"""

from sys import stdin
from math_lib import *


def arithmetic_mean(values):
    """ Calculate arithmetic mean

    @param values: list of input values
    @return: arithmetic mean
    """
    mean = 0
    for value in values:
        mean = func_sum(mean, value)

    mean = div(mean, len(values))

    # return arithmetic mean
    return mean


def standard_deviation(values, mean):
    """ Calculate standard deviation

    @param values: list of input values
    @param mean: arithmetic mean
    @return: calculated standard deviation
    """
    deviation = 0
    N = len(values)

    for value in values:
        deviation = func_sum(power(value), deviation)

    deviation = sub(deviation, multi(N, power(mean)))
    deviation = multi(div(1, sub(N, 1)), deviation)
    deviation = root(deviation)
    return deviation


def read_from_input():
    """ Read input and calculate standard deviation

    @return: standard deviation
    """
    # form input read value and append it to the list of values
    values = [float(line) for line in stdin]

    # calculate arithmetic mean
    mean = arithmetic_mean(values)

    # calculate standard deviation
    deviation = standard_deviation(values, mean)

    return deviation


print(read_from_input())
