'''
Created on Mar 17, 2015

@author: PCX
'''
from test import test_data
import unittest

from generator import app_generator

class Test(unittest.TestCase):

    def setUp(self):
        self.app_model = test_data.test_app_model
        app_generator.generate("test_gen", self.app_model)

    def test_generator(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
