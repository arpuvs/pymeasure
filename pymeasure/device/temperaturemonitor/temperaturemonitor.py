__author__ = 'matsumototakao'

#! /usr/bin/env python
# coding=utf-8

import os
import sys
import time
import threading
import socket

from .. import device

#=======================
# Interface Class
#=======================

class temperaturemonitor(device.device):
    # property configuration
    # ======================

    temp = 0

    # constructor
    # ===========
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.model_check()
        pass

    # interface method
    # ================
    def measure(self, input):
        self.temp = self._temp_get(input)
        return self.temp

    def measure_all(self, 0):
        self.temp = self._measure_all(0)
        return self.temp

    def calibration(self, standard_curve, user_curve, serial_number, first_temp, first_sensor_units, second_temp, second_sensor_units, third_temp, third_sensor_units,):
        self._calibration(standard_curve, user_curve, serial_number, first_temp, first_sensor_units, second_temp, second_sensor_units, third_temp, third_sensor_units,)
        return

    def curve_set(self, input, curve_number):
        self._curve_set(input, curve_number)
        return

    def curve_check(self, input):
        curve = self._curve_check(input)
        return curve

    def model_check(self):
        self.model = self._model_check()
        return

    def preset(self):
        self._preset()
        return



    # self test
    # =========
    def self_test(self ,interval=0.2):
        wait = lambda: time.sleep(interval)

        print('self_test :: TemperatureMonitor')
        print('===============================')
        print('model: %s'%(self.model))
        print('communicator: %s'%(self.com.method))
        print('==================================')
        print('')
        print('self_test start')
        print('')
        print('%-75s'%"measure(1):"),
        try:
            ret = self.measure(1)
            wait()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f' %(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__,err[1]))
            pass

        print('%-75s'%"measure_all():"),
        try:
            ret = self.measure_all()
            wait()
            if type(ret)!=str: print('!! Bad !!, return is not string')
            else: print('OK, %s'%(ret))
        except:
            err =sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-75s'%"calibration(1, 21, SC12345, 4.2, 1.6260, 77.32, 1.0205, 300.0, 0.5189):")
        try:
            self.calibration(1, 21, SC12345, 4.2, 1.6260, 77.32, 1.0205, 300.0, 0.5189)
            wait(0.8)
            print('OK')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-75s'%"curve_set(1, 1):"),
        try:
            self.curve_set(1, 1)
            wait()
            ret = self.curve_check(1)
            if type(ret)!=int: print('!! Bad !!, return is not integer')
            else: print('OK, %d'%(ret))
        except:
            err =sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-75s'%"curve_check(1):"),
        try:
            ret = self.curve_check(1)
            wait()
            if type(ret)!=int: print('!! Bad !!, return is not integer')
            else: print('OK, %d'%(ret))
        except:
            err =sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('')
        print('finalize')
        print('--------')
        print('preset()')
        self.preset()
        print('')
        return

    # internal method
    # ===============
    def _measure(self, input):
        return float()

    def _measure_all(self, 0):
        return str()

    def _calibration(self, standard_curve, user_curve, serial_number, first_temp, first_sensor_units, second_temp, second_sensor_units, third_temp, third_sensor_units,):
        return None

    def _curve_set(self, input, curve_number):
        return None

    def _curve_check(self, input):
        return int

    def _model_check(self):
        return str()

# ====================
# Dummy Server/Client
# ====================

dummy_api = {'measure': 'dummy_pm:measure',
             'measure_all': 'dummy_pm:measure_all',
             'calibration': 'dummy_pm:calibration'}


# dummy client
# ============
class dummy_client(temperaturemonitor):
    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        temperaturemonitor.__init__(self, com)
        pass

    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return

    def _measure(self, input):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['measure']))
        temp = self.com.readline()
        self.com.close()
        return temp

    def _measure_all(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['measure_all']))
        temp = str(self.com.readline().split(' '))
        self.com.close()
        return temp

    def _calibration(self, standard_curve, user_curve, serial_number, first_temp, first_sensor_units, second_temp, second_sensor_units, third_temp, third_sensor_units,):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['calibration']))
        self.com.close()
        return

    def _curve_set(self, input, curve_number):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['curve_set']))
        self.com.close()
        return

    def _curve_check(self, input):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['curve_check']))
        curve_number =
        self.com.close()
        return

    def _model_check(self):
        return 'PowerMeter_Dummy'












