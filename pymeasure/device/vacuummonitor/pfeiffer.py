__author__ = 'matsumototakao'

#! /usr/bin/env python

import vacuummonitor as vm

api = {'bar': 0,
       'torr': 1,
       'pascal': 2}

class pfeiffer(vm.vacuummonitor):
    # property configuration
    press = []

    # internal method
    # ===============
    def _measure(self):
        self.com.open()
        self.com.send('PRX\n')
        ret = self.com.readline().strip().split(',')
        del ret[1]
        del ret[2]
        press =str(ret)
        self.com.close()
        return press

    def _unit_check(self):
        self.com.open()
        self.com.send('PRX\n')
        ret = self.com.readline().strip().split(',')
        del ret[0]
        del ret[1]
        unit = str(ret)
        self.com.close()
        return unit

    def _unit_set(self, unit):
        self.com.open()
        if unit.lower()=='bar': self.com.send('UNI,%d'%(api['bar']))
        elif unit.lower()=='torr': self.com.send('UNI,%d'%(api['torr']))
        elif unit.lower()=='pascal': self.com.send('UNI,%d'%(api['pascal']))
        else: print('unit is incorrect!')
        self.com.close()
        return

class D35614asslar(pfeiffer):
    pass


