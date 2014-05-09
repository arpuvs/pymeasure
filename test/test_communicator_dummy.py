#! /usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

import pymeasure.communicator.dummy as com
from test_communicator import TestCommunicator
import unittest

class TestCommunicatorDummy(TestCommunicator, unittest.TestCase):
    def setUp(self):
        self.com = com.dummy_communicator()
        self.com.open()
        return

if __name__=='__main__':
    unittest.main()
