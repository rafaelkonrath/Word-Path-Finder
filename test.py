#!/usr/bin/env python

import unittest
from wordpaths import main

class Test(unittest.TestCase):

    def setUp(self):
        self.valid_starts = ['cat','fike']
        self.valid_ends = ['dog','camp']

    def test(self):
        for i in xrange(len(self.valid_starts)):
            path = main(['/usr/share/dict/words',self.valid_starts[i],self.valid_ends[i]])

if __name__ == '__main__':
    unittest.main()
