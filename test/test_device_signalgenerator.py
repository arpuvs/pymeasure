#! /usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

import pymeasure.communicator.dummy as com
import pymeasure.device.signalgenerator.signalgenerator as sg
import unittest

class TestSignalgenerator(unittest.TestCase):
    
    def setUp(self):
        _com = com.dummy_communicator()
        self.dev = sg.dummy(_com)
        return
    
    def tearDown(self):
        return
    
    def test_freq_set(self):
        def check(freq, unit):
            self.dev.freq_set(freq, unit)
            ret = self.dev.freq_check()
            self.assertEqual(freq*self.dev.freq_unit[unit.lower()], ret)
            return
        
        check(11111111, 'Hz')
        check(2222, 'MHz')
        check(3.33, 'ghz')
        return

    def test_freq_check(self):
        self.dev.freq_set(1e5)
        self.assertIsInstance(self.dev.freq_check(), float)
        return
    
    def test_power_set(self):
        def check(power):
            self.dev.power_set(power)
            ret = self.dev.power_check()
            self.assertEqual(power, ret)
            return
        
        check(-40)
        check(-50.5)
        check(-60.666)
        return

    def test_power_check(self):
        self.dev.power_set(-50.0)
        self.assertIsInstance(self.dev.power_check(), float)
        return
        
    def test_output_on(self):
        self.dev.output_on()
        self.assertEqual(self.dev.output_check(), 1)
        return

    def test_output_off(self):
        self.dev.output_off()
        self.assertEqual(self.dev.output_check(), 0)
        return

    def test_output_check(self):
        self.dev.output_off()
        self.assertIsInstance(self.dev.output_check(), int)
        return


if __name__=='__main__':
    unittest.main()
