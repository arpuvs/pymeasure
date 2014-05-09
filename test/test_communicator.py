#! /usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

import pymeasure.communicator.communicator as com
import unittest

class TestCommunicator(object):
    com = None
    
    def setUp(self):
        #self.com = com.communicator()
        #self.com.open()
        return
    
    def tearDown(self):
        self.com.close()
        return

    def test_send(self):
        self.assertTrue(self.com.send('test\n'))
        self.assertTrue(self.com.send('123456\n'))
        self.assertTrue(self.com.send('\x01\x12\xF0\x20'))
        return
    
    def test_recv(self):
        self.assertTrue(0 < len(self.com.recv(3)) < 4)
        self.assertTrue(0 < len(self.com.recv(10)) < 11)
        self.assertTrue(0 < len(self.com.recv(20)) < 21)
        return

    def test_readline(self):
        self.assertTrue(0 < len(self.com.readline()))
        return
    
        
