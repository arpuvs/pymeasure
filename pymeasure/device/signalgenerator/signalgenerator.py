#! /usr/bin/env python

import os
import sys
import time
import threading
import socket

from .. import device


# ===============
# Interface Class
# ===============
class signalgenerator(device.device):
    # property configuration
    # ======================
    freq = None
    power = None
    output = None
    
    freq_unit = {'hz': 1, 'khz': 1e3, 'mhz': 1e6, 'ghz': 1e9}
    
    # constructor
    # ===========
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.freq_check()
        self.power_check()
        self.output_check()
        self.model_check()
        pass
    
    # interface method
    # ================
    def freq_set(self, freq, unit='MHz'):
        """
        """
        self._freq_set(freq, unit)
        self.freq = freq * self.freq_unit[unit.lower()]
        return
    
    def freq_check(self):
        """
        """
        self.freq = self._freq_check()
        return self.freq
        
    def power_set(self, power, unit='dBm'):
        """
        """
        self._power_set(power, unit)
        self.power = power
        return
    
    def power_check(self):
        """
        """
        self.power = self._power_check()
        return self.power
    
    def output_on(self):
        """
        """
        self._output_on()
        self.output = 1
        return
    
    def output_off(self):
        """
        """
        self._output_off()
        self.output = 0
        return
    
    def output_check(self):
        """
        """
        self.output = self._output_check()
        return self.output
    
    def model_check(self):
        self.model = self._model_check()
        return
        
    def preset(self):
        return None
    
    # self test
    # =========
    def self_test(self, interval=0.2):
        wait = lambda: time.sleep(interval)
        
        print('self_tset :: signalgenerator')
        print('============================')
        print('model: %s'%(self.model))
        print('communicator: %s'%(self.com.method))
        print('----------------------------')
        
        print('initialize')
        print('----------')
        print('output_off()')
        self.output_off()
        wait()
        
        print("power_set(-80, 'dBm')")
        self.power_set(-80, 'dBm')
        wait()
        
        print('')
        print('test start')
        print('----------')
        
        print('%-30s'%'freq_check():'),
        try:
            ret = self.freq_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-30s'%"freq_set(100, 'MHz'):"),
        try:
            self.freq_set(100, 'MHz')
            wait()
            ret = self.freq_check()
            if ret!=100*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%"freq_set(12.34, 'MHz'):"),
        try:
            self.freq_set(12.34, 'MHz')
            wait()
            ret = self.freq_check()
            if ret!=12.34*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%"freq_set(9.8765432101, 'GHz'):"),
        try:
            self.freq_set(9.8765432101, 'GHz')
            wait()
            ret = self.freq_check()
            if ret!=9.8765432101*1e9: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-30s'%'power_check():'),
        try:
            ret = self.power_check()
            wait()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-30s'%"power_set(-20, 'dBm'):"),
        try:
            self.power_set(-20, 'dBm')
            wait()
            ret = self.power_check()
            if ret!=-20: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%"power_set(-43.21, 'dBm'):"),
        try:
            self.power_set(-43.21, 'dBm')
            wait()
            ret = self.power_check()
            if ret!=-43.21: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%'output_check():'),
        try:
            ret = self.output_check()
            wait()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-30s'%"output_on():"),
        try:
            self.output_on()
            wait()
            ret = self.output_check()
            if ret!=1: print('!! Bad !!, %d'%(ret))
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        print('%-30s'%"output_off():"),
        try:
            self.output_off()
            wait()
            ret = self.output_check()
            if ret!=0: print('!! Bad !!, %d'%(ret))
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('')

        print('finalize')
        print('----------')
        print('output_off()')
        self.output_off()
        print("power_set(-80, 'dBm')")
        self.power_set(-80, 'dBm')
        wait()
        print("preset()")
        self.preset()
        
        print('')
        return


    
    # internal method
    # ===============
    def _freq_set(self, freq, unit):
        return None
    
    def _freq_check(self):
        return float()
    
    def _power_set(self, power, unit):
        return None
    
    def _power_check(self):
        return float()
    
    def _output_on(self):
        return None

    def _output_off(self):
        return None
        
    def _output_check(self):
        return int()
        
    def _model_check(self):
        return str()

        
# ===================
# Dummy Server/Client
# ===================
dummy_api = {'freq_set': 'dummy_sg:freq_set',
             'freq_check': 'dummy_sg:freq_check',
             'power_set': 'dummy_sg:power_set',
             'power_check': 'dummy_sg:power_check',
             'output_set': 'dummy_sg:output_set',
             'output_check': 'dummy_sg:output_check'}

# dummy client
# ============
class dummy_client(signalgenerator):
    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        signalgenerator.__init__(self, com)
        pass
        
    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return
        
    def _freq_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %.10f %s\n'%(dummy_api['freq_set'], freq, unit))
        self.com.close()
        return
    
    def _freq_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['freq_check']))
        freq = float(self.com.readline())
        self.com.close()
        return freq
        
    def _power_set(self, power, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(dummy_api['power_set'], power, unit))
        self.com.close()
        return
    
    def _power_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['power_check']))
        power = float(self.com.readline())
        self.com.close()
        return power
        
    def _output_on(self):
        self.com.open()
        self.com.send('%s 1\n'%(dummy_api['output_set']))
        self.com.close()
        return
        
    def _output_off(self):
        self.com.open()
        self.com.send('%s 0\n'%(dummy_api['output_set']))
        self.com.close()
        return
    
    def _output_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['output_check']))
        output = int(self.com.readline())
        self.com.close()
        return output
        
    def _model_check(self):
        return 'SignalGenerator_Dummy'


# dummy server
# ============
class dummy_server(object):
    freq = 0
    power = 0
    output = 0
    freq_unit = {'hz': 1, 'khz': 1e3, 'mhz': 1e6, 'ghz': 1e9}
    
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
        if command==dummy_api['freq_set']: self.freq_set(params)
        elif command==dummy_api['freq_check']: self.freq_check(params)
        elif command==dummy_api['power_set']: self.power_set(params)
        elif command==dummy_api['power_check']: self.power_check(params)
        elif command==dummy_api['output_set']: self.output_set(params)
        elif command==dummy_api['output_check']: self.output_check(params)
        else: print(command, params)
        return
        
    def freq_set(self, params):
        val = float(params[0])
        unit = params[1].lower()
        self.freq = val * self.freq_unit[unit]
        return
        
    def freq_check(self, params):
        self.client.send('%.10f\n'%(self.freq))
        return
        
    def power_set(self, params):
        val = float(params[0])
        unit = params[1].lower()
        self.power = val
        return
        
    def power_check(self, params):
        self.client.send('%f\n'%(self.power))
        return
        
    def output_set(self, params):
        val = int(params[0])
        self.output = val
        return
        
    def output_check(self, params):
        self.client.send('%d\n'%(self.output))
        return

        
    
