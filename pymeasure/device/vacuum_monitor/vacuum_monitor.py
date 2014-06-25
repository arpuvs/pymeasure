#! /usr/bin/env python
# coding=utf-8

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))

import device

class vacuum_monitor(device.device):
    api = {'pressure_get': ''}
    pressure = None

    def pressure_get(self):

        self.pressure = self._pressure_get()
        return self.pressure

    def _pressure_get(self):

        self.com.open()
        self.com.send('%s¥n'%(self.api['pressure_get']))
        pressure = float(self.com.readline())
        self.com.close()
        return pressure


class dummy(vacuum_monitor):
    pressure = None

    def _pressure_get(self):
        self.com.open()
        self.com.send('%s¥n'%(self.api['pressure_get']))
        self.com.close()
        return self.pressure
