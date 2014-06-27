#! /usr/bin/env python

import os
import sys
import time
import random
import threading
import socket

from .. import device


# ===============
# Interface Class
# ===============
class powermeter(device.device):
    # property configuration
    # ======================
    power = []
    
    # constructor
    # ===========
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.measure()
        self.model_check()
        pass
    
    # interface method
    # ================
    def measure(self):
        """
        """
        self.power = self._measure()
        return self.power
    
    def zeroing(self):
        """
        """
        self._zeroing()
        return
    
    def calibration(self):
        """
        """
        self._calibration()
        return
    
    def model_check(self):
        """
        """
        self.model = self._model_check()
        return
        
    def preset(self):
        """
        """
        self._preset()
        return
    
    # self test
    # =========
    def self_test(self, interval=0.2):
        def wait(sec=interval):
            time.sleep(sec)
            return
        
        print('self_tset :: powermeter')
        print('============================')
        print('model: %s'%(self.model))
        print('communicator: %s'%(self.com.method))
        print('----------------------------')
        
        print('initialize')
        print('----------')
        print("preset()")
        self.preset()
        wait()
        print('')
        
        print('test start')
        print('----------')
        
        print('%-20s'%'measure():'),
        try:
            ret = self.measure()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            else: print('OK, %s'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-20s'%'zeroing():'),
        try:
            ret = self.zeroing()
            wait(0.8)
            print('OK,')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-20s'%'calibration():'),
        try:
            ret = self.calibration()
            wait(0.8)
            print('OK,')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('')
        
        print('finalize')
        print('----------')
        wait()
        print("preset()")
        self.preset()
        
        print('')
        return
    
    # internal method
    # ===============
    def _measure(self):
        return [float(),]
    
    def _zeroing(self):
        return None
    
    def _calibration(self):
        return None
    
    def _model_check(self):
        return str()
        
    def _preset(self):
        return None



# ===================
# Dummy Server/Client
# ===================
dummy_api = {'measure': 'dummy_pm:measure',
             'zeroing': 'dummy_pm:zeroing',
             'calibration': 'dummy_pm:calibration'}

# dummy client
# ============
class dummy_client(powermeter):
    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        powermeter.__init__(self, com)
        pass
        
    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return
        
    def _measure(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['measure']))
        power = map(float, self.com.readline().split(' '))
        self.com.close()
        return power
    
    def _zeroing(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['zeroing']))
        self.com.close()
        return 
        
    def _calibration(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['calibration']))
        self.com.close()
        return
    
    def _model_check(self):
        return 'PowerMeter_Dummy'


# dummy server
# ============
class dummy_server(object):
    power = [-12.34, -56.78]
    
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
                command = data.strip().split(' ')[0]
                params = data.strip().split(' ')[1:]
                self.handle(command, params)
                continue
            
            client.close()
            continue
        return
    
    def handle(self, command, params):
        if command==dummy_api['measure']: self.measure(params)
        elif command==dummy_api['zeroing']: self.zeroing(params)
        elif command==dummy_api['calibration']: self.calibration(params)
        else: print(command, params)
        return
        
    def measure(self, params):
        ch1 = random.randrange(-800, +100) / 10.
        ch2 = ch1 * random.randrange(8, 12) / 10.
        self.client.send('%.3f %.3f\n'%(ch1, ch2))
        return
        
    def zeroing(self, params):
        return
        
    def calibration(self, params):
        return
        

        
    
