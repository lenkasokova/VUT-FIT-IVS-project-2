# -*- coding: utf-8 -*-
"""

@author: Andrej Bínovský (xbinov00)

Test math_lib for project n.2 - IVS 2021

"""
import unittest
import math_lib


class TestMathLib(unittest.TestCase):
    numbers_1 = [12, -55, 8, 3, 1987, 330.5, 918, -13.1, 43, 6.5, 4, 9]
    numbers_2 = [-12.567, 32.1, 46, 88, 13, -18, 24, 54, 8, 1, 0, -1.4]

    # TESTING SUM
    def test_sum(self):
        numbers_sum = [-0.567, -22.9, 54, 91, 2000, 312.5, 942, 40.9, 51, 7.5, 4, 7.6]

        for i in range(12):
            self.assertEqual(math_lib.func_sum(self.numbers_1[i], self.numbers_2[i]), numbers_sum[i])

    # TESTING SUBTRACTION
    def test_sub(self):
        numbers_sub_1 = [24.567, -87.1, -38, -85, 1974, 348.5, 894, -67.1, 35, 5.5, 4, 10.4]
        numbers_sub_2 = [-24.567, 87.1, 38, 85, -1974, -348.5, -894, 67.1, -35, -5.5, -4, -10.4]

        for i in range(12):
            self.assertEqual(math_lib.sub(self.numbers_1[i], self.numbers_2[i]), numbers_sub_1[i])
            self.assertEqual(math_lib.sub(self.numbers_2[i], self.numbers_1[i]), numbers_sub_2[i])

    # TESTING DIVIDING
    def test_div(self):
        numbers_div = [-1.04725, -0.583636, 5.75, 29.333333, 0.006543, -0.054463, 0.026144, -4.122137, 0.186047, 0.153846, 0.0, -0.155556]

        for i in range(12):
            self.assertEqual(math_lib.div(self.numbers_2[i], self.numbers_1[i]), numbers_div[i])

        # TESTING ERRORS
        self.assertEqual(math_lib.div(5, 0), ValueError)
        self.assertEqual(math_lib.div(-5, 0), ValueError)

    # TESTING MULTIPICATION
    def test_multi(self):
        numbers_mutli = [-150.804, -1765.5, 368, 264, 25831, -5949.0, 22032, -707.4, 344, 6.5, 0, -12.6]
        for i in range(12):
            self.assertEqual(math_lib.multi(self.numbers_1[i], self.numbers_2[i]), numbers_mutli[i])
            self.assertEqual(math_lib.multi(self.numbers_2[i], self.numbers_1[i]), numbers_mutli[i])

    # TESTING FACTIORIAL
    def test_fact(self):
        numbers_fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800]
        for i in range(12):
            self.assertEqual(math_lib.fact(i), numbers_fact[i])

        # TESTING ERRORS
        self.assertEqual(math_lib.fact(-1), ValueError)
        self.assertEqual(math_lib.fact(0.1), ValueError)
        self.assertEqual(math_lib.fact(1.5), ValueError)

    # TESTING POWER

    def test_power(self):
        numbers_1 = [12, -55, 8, 3, 1987, 330.5, 918, -13.1, 43, 6.5, 4, 9]
        for i in range(12):
            # test ^0
            self.assertEqual(math_lib.power(numbers_1[i], 0), 1)
            # test ^1
            self.assertEqual(math_lib.power(numbers_1[i], 1), round(numbers_1[i], 6))
            # test ^2
            self.assertEqual(math_lib.power(numbers_1[i], 2), round((numbers_1[i]*numbers_1[i]), 6))
            # test ^3
            self.assertEqual(math_lib.power(numbers_1[i], 3), round((numbers_1[i]*numbers_1[i]*numbers_1[i]), 6))
            # test ^-1
            self.assertEqual(math_lib.power(numbers_1[i], -1), round((1/numbers_1[i]), 6))
            # test ^-2
            self.assertEqual(math_lib.power(numbers_1[i], -2), round((1/(numbers_1[i]*numbers_1[i])), 6))

        # TESTING FLOATING POINT
        self.assertEqual(math_lib.power(5, 1.5), 11.18034)
        self.assertEqual(math_lib.power(9, 0.5), 3)

        # TESTING ZERO
        self.assertEqual(math_lib.power(0, 4), 0)

        # TESTING ERRORS
        self.assertEqual(math_lib.power(0, -1), ValueError)

    # TESTING ROOT
    def test_root(self):
        numbers_root = [4, 2, 25, 644, 1987, 330.5, 918, 13.1, 43, 6.5, 49, 9]
        numbers_results = [2, 1.414214, 5, 25.377155, 44.575778, 18.179659, 30.298515, 3.619392, 6.557439, 2.54951, 7, 3]
        for i in range(12):
            self.assertEqual(math_lib.root(numbers_root[i]), numbers_results[i])

        # TESTING ANOTHER ROOTS
        self.assertEqual(math_lib.root(8, 3), 2)
        self.assertEqual(math_lib.root(16, 4), 2)
        self.assertEqual(math_lib.root(100, 5), 2.511886)
        self.assertEqual(math_lib.root(9, 0.5), 81)
        self.assertEqual(math_lib.root(5, -1), 0.2)
        self.assertEqual(math_lib.root(8, -3), 0.5)

        # TESTING ERRORS
        self.assertEqual(math_lib.root(-5, 2), ValueError)
        self.assertEqual(math_lib.root(-5, -2), ValueError)
        self.assertEqual(math_lib.root(5, 0), ValueError)
    
    # TESTING SIN
    def test_func_sin(self):
        self.assertEqual(math_lib.func_sin(0), 0)
        self.assertEqual(math_lib.func_sin(30), 0.5)
        self.assertEqual(math_lib.func_sin(45), 0.707107)
        self.assertEqual(math_lib.func_sin(90), 1)

    # TESTING COS
    def test_func_cos(self):
        self.assertEqual(math_lib.func_cos(0), 1)
        self.assertEqual(math_lib.func_cos(30), 0.866025)
        self.assertEqual(math_lib.func_cos(45), 0.707107)
        self.assertEqual(math_lib.func_cos(90), 0)

    # TESTING TAN
    def test_func_tan(self):
        self.assertEqual(math_lib.func_tan(0), 0)
        self.assertEqual(math_lib.func_tan(30), 0.57735)
        self.assertEqual(math_lib.func_tan(45), 1)
        self.assertEqual(math_lib.func_tan(90), ValueError)
        self.assertEqual(math_lib.func_tan(-270), ValueError)

    # TESTING COTAN
    def test_func_cotan(self):
        self.assertEqual(math_lib.func_cotan(0), ValueError)
        self.assertEqual(math_lib.func_cotan(30), 1.732051)
        self.assertEqual(math_lib.func_cotan(45), 1)
        self.assertEqual(math_lib.func_cotan(90), 0)
        self.assertEqual(math_lib.func_cotan(180), ValueError)
    
    # TESTING NUMBER
        self.assertEqual(math_lib.func_cotan('a'), ValueError)
        self.assertEqual(math_lib.fact("test"), ValueError)
        self.assertEqual(math_lib.sub("test", "test"), ValueError)


if __name__ == '__main__':
    unittest.main()

