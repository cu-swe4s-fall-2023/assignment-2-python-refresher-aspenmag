import sys
import numpy as np
import random
import os
import unittest
from numpy.random import randint
sys.path.insert(0, '../../src')  # noqa # must run from unit test directory
import my_utils as u  # noqa
import box as b
import correlation as c
import hist as h


class TestMathLib(unittest.TestCase):
    def setUP(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')

        for i in range(100):
            rand_int = random.randint(1, 100)
            f.write(str(rand_int) + str(rand_int) + str(rand_int) + '\n')
        f.close()


# note to self: we have already tested get_col, so just do plotting

def test_box_pos(self):
    rand_dat = randint(0, 100000, 1000)
    b.box_plt(rand_dat, 'random values', 'frequency',
              'random_box_test.png')
    self.assertEqual('random_box_test.png',  'random_box_test.png')


def test_his_pos(self):
    rand_dat = randint(0, 100000, 1000)
    h.hist(rand_dat, 'random values', 'frequency',
           'random_hist_test.png')
    self.assertEqual('random_hist_test.png',  'random_hist_test.png')


def test_cor_pos(self):
    rand_dat = randint(0, 100000, 1000)
    rand_dat2 = randint(0, 100000, 1000)
    c.correlation_plt(rand_dat, rand_dat2, 'random values',
                      'frequency', 'random_cor_test.png')
    self.assertEqual('random_hist_test.png',  'random_hist_test.png')


def test_box_er(self):
    rand_dat = randint(0, 100000, 1000)
    self.assertRaises(TypeError, b.box_plt, rand_dat,
                      'random values', 'frequency')


def test_hist_er(self):
    rand_dat = randint(0, 100000, 1000)
    self.assertRaises(TypeError, h.hist, rand_dat,
                      'random values', 'frequency')


def test_cor_er(self):
    rand_dat = randint(0, 100000, 1000)
    rand_dat2 = randint(0, 100000, 1000)
    self.assertRaises(TypeError, c.correlation_plt, rand_dat, rand_dat2,
                      'random values', 'frequency')


if __name__ == '__main__':
    unittest.main()
