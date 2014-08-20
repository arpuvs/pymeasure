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
    #property configuration
    # =====================
    pressure = None


    # constructor
    # ============
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.press_get()
        self.model_check()
        pass

    #Interface method
    # ===============
    def press_get(self):
        """
        """
        self.press = self._press_get()
        return self.press

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
        print('press_get()')
        try:
            ret = self.press_get()
            if type(ret)!=float: print('!! Bad !!, return in not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        wait()

        print('test end')
        print('')
        return


    # internal method
    # ===============

    def _press_get(self):
        return float()

    def _model_check(self):
        return str()



# ====================
# Dummy Server/Client
# ====================
dummy_api = {'press_get': 'dummy_vm:press_get'}

# dummy client
# ============
class dummy_client(vacuummonitor):
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

    def _press_get(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['press_get']))
        press = float(self.com.readline())
        self.com.close()
        return press

    def _model_check(self):
        return 'VacuumMonitor_Dummy'



# dummy server
# ============
class dummy_server(object):
    press = 0

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
        if command==dummy_api['press_get']: self.press_get(params)
        else: print(command, params)
        return

    def press_get(self, params):
        self.client.send('%.10f\n'%(self.press))
        return

