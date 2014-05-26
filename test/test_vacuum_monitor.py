#! /usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

import pymeasure.communicator.dummy as com
import pymeasure.device.vacuum_monitor.vacuum_monitor as vm
import unittest

class TestVacuummonitor(unittest.TestCase):

    def setUp(self):
        _com = com.dummy_communicator()
        self.dev = vm.dummy(_com)
        return

    def tearDown(self):
        return

    def test_pressure_get(self):
        self.assertIsInstance(self.dev.pressure_get(), float)
        return

if __name__=='__main__':
    unittest.main()



