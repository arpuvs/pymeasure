__author__ = 'matsumototakao'

#! /usr/bin/env python

import vacuummonitor as vm

_unit = {'bar': 0,
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
        press = [ret[1], ret[3]]
        self.com.close()
        return press

    def _unit_check(self):
        return self.unit

    def _unit_set(self, unit):
        self.com.open()
        self.com.send('UNI,%d'%(_unit[unit]))
        self.unit = str(self.com.readline().strip())
        self.com.close()
        return self.unit

class D35614asslar(pfeiffer):
    pass


