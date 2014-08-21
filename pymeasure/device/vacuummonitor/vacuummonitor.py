#! /usr/bin/env python
# coding=utf-8

import os
import sys
import time
import threading
import socket

from .. import device

# ======================
# Interface Class
# ======================

class vacuummonitor(device.device):
    # property configuration
    # ======================
    press1 = 0
    press2 = 0
    unit1 = 'None'
    unit2 = 'None'
    gauge = 0
    press = []
    unit = 'None'

    # constructor
    # ============
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.measure()
        self.unit_check()
        self.model_check()
        pass

    # Interface method
    # ================
    def measure(self):
        """
        """
        self.press = self._measure()
        return self.press

    def unit_set(self, gauge, unit):
        """
        """
        self._unit_set(gauge, unit)
        self.unit = self._unit_check()
        return

    def unit_check(self):
        """
        """
        self.unit = self._unit_check()
        return self.unit


    def model_check(self):
        self.model = self._model_check()
        return



    # self test
    # =========
    def self_test(self, interval=0.2):
        wait = lambda: time.sleep(interval)

        print('self_test :: vacuummonitor')
        print('==========================')
        print('model: %s'%(self.model))
        print('communicator: %s'%(self.com.method))
        print('--------------------------')

        print('')
        print('test start')
        print('----------')
        print('%-10s'%'measure():'),
        try:
            ret = self.measure()
            wait()
            if type(ret)!=str: print('!! Bad !!, return is not str')
            else: print('OK, %s'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%'unit_check():'),
        try:
            ret = self.unit_check()
            wait()
            if type(ret)!=str: print('!! Bad !!, return is not str')
            else: print('OK, %s'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%'unit_set():'),
        try:
            self.unit_set(1, 'torr')
            wait()
            ret = self.unit_check()
            if ret!="['torr', 'None']": print('!! Bad !!, %s'%(ret))
            else: print('OK, %s'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s %s'%(err[0].__name__, err[1]))
            pass



        wait()

        print('')
        print('test end')
        print('')
        return


    # internal method
    # ===============

    def _measure(self):
        return str()

    def _unit_set(self, gauge, unit):
        return None

    def _unit_check(self):
        return str()

    def _model_check(self):
        return str()



# ====================
# Dummy Server/Client
# ====================
dummy_api = {'measure': 'dummy_vm:measure',
             'unit_set': 'dummy_vm:unit_set',
             'unit_check': 'dummy_vm:unit_check'}

# dummy client
# ============
class dummy_client(vacuummonitor):

    # property configuration
    # ======================

    unit = 'None'
    press = []

    # method
    # ======

    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        vacuummonitor.__init__(self, com)
        pass

    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return

    def _measure(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['measure']))
        press = str(self.com.readline().strip().split(' '))
        self.com.close()
        return press

    def _unit_set(self, gauge, unit):
        self.com.open()
        self.com.send('%s %s %s\n'%(dummy_api['unit_set'], gauge, unit))
        self.com.close()
        return

    def _unit_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['unit_check']))
        unit = str(self.com.readline().strip().split(' '))
        self.com.close()
        return unit

    def _model_check(self):
        return 'VacuumMonitor_Dummy'



# dummy server
# ============
class dummy_server(object):
    press1 = 0
    press2 = 0
    unit1 = 'None'
    unit2 = 'None'
    gauge = 0
    unit = 'None'

    def __init__(self, port):
        self.port = port
        self.start()
        pass

    def start(self):
        threading.Thread(target=self._start).start()
        return

    def _start(self):
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', self.port))
        server.listen(1)



        while True:
            client, client_address = server.accept()
            self.client = client

            while True:
                data = client.recv(8192)
                if len(data)==0: break
                if data=='stop\n': return
                command =data.strip().split(' ')[0]
                params = data.strip().split(' ')[1:]
                self.handle(command, params)
                continue

            client.close()
            continue
        return

    def handle(self, command, params):
        if command==dummy_api['measure']: self.measure(params)
        elif command==dummy_api['unit_check']: self.unit_check(params)
        elif command==dummy_api['unit_set']: self.unit_set(params)
        else: print(command, params)
        return

    def measure(self, params):
        self.client.send('%.10f %.10f\n'%(self.press1, self.press2))
        return

    def unit_check(self, params):
        self.client.send('%s %s\n'%(self.unit1, self.unit2))
        return

    def unit_set(self, params):
        gauge = int(params[0])
        self.unit1 = str(params[1].lower())
        return







