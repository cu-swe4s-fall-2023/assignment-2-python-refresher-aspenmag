import sys
import numpy as np
import random
import os
import unittest
from numpy.random import randint
sys.path.insert(0, '../src')  # noqa # must run from unit test directory
import my_utils as u  # noqa
#  NOTE TO SELF : i think that this will go from the unit test directory back
#  one to the home directory where the utility functions are


class TestMathLib(unittest.TestCase):
    def setUP(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')

        for i in range(100):
            rand_int = random.randint(1, 100)
            f.write(str(rand_int) + str(rand_int) + str(rand_int) + '\n')
        f.close()

    def test_getcol_pos(self):
        query_col = randint(0, 2)  # test file has 3 columns
        query_val = randint(0, 100)
        result_col = randint(0, 2)

        f = open('testing_data_file.txt', 'w')
        for i in range(100):
            rand_int = random.randint(1, 100)
            f.write(str(rand_int) + ',' + str(rand_int) + ',' + str(rand_int)
                    + '\n')
        f.close()
        val = u.get_column('testing_data_file.txt', query_col, query_val,
                           result_col)
        self.assertIsNotNone(val)

    def test_getcol_er(self):
        query_col = randint(0, 2)  # test file has 3 columns
        query_val = randint(0, 100)
        result_col = randint(0, 2)

        val = u.get_column('nonexistent_silly_file.txt', query_col, query_val,
                           result_col)
        self.assertRaises(FileNotFoundError)

    def test_mean_pos(self):
        a = randint(0, 100, 100)
        mean_func = u.mean(a)
        mean_np = np.mean(a)
        self.assertEqual(mean_np, mean_func)

    def test_mean_er(self):
        a = []
        mean_func = u.mean(a)
        mean_np = np.mean(a)
        self.assertTrue(mean_np, mean_func)

    def test_median_pos(self):
        a = randint(0, 100, 100)
        med_func = u.median(a)
        med_np = np.median(a)
        self.assertEqual(med_np, med_func)

    def test_med_er(self):
        a = []
        med_func = u.median(a)
        med_np = np.median(a)
        self.assertTrue(med_np, med_func)

    def test_stdv_pos(self):
        a = randint(0, 100, 100)
        stdv_func = u.stdv(a)
        stdv_np = np.std(a)
        # note: here use amost equal to account for long decimal numbers
        self.assertAlmostEqual(stdv_np, stdv_func)

    def test_std_er(self):
        a = []
        stdv_func = u.stdv(a)
        stdv_np = np.std(a)
        self.assertTrue(stdv_np, stdv_func)


if __name__ == '__main__':
    unittest.main()
