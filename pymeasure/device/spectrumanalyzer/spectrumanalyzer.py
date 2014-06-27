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
class spectrumanalyzer(device.device):
    # property configuration
    # ======================
    freq_center = None
    freq_start = None
    freq_stop = None
    freq_span = None
    full_span = None
    zero_span = None
    sweeppoints = None
    sweeptime = None
    attenuation = None
    referenceoevel = None
    scaledivision = None
    average = None
    resolutionBW = None
    videoBW = None
    
    freq_unit = {'hz': 1, 'khz': 1e3, 'mhz': 1e6, 'ghz': 1e9}

    # constructor
    # ===========
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.refresh()
        self.model_check()
        pass
    
    # interface method
    # ================
    def refresh(self):
        self.freq_center_check()
        self.freq_start_check()
        self.freq_stop_check()
        self.freq_span_check()
        self.resolutionBW_check()
        self.videoBW_check()
        self.sweeppoints_check()
        self.sweeptime_check()
        self.attenuation_check()
        self.referencelevel_check()
        self.average_check()
        return
        
    def measure(self):
        """
        """
        spectrum = self._measure()
        return spectrum
    
    def freq_center_check(self):
        """
        """
        self.freq_center = self._freq_center_check()
        return self.freq_center
    
    def freq_center_set(self, freq, unit='MHz'):
        """
        """
        self._freq_center_set(freq, unit)
        self.refresh()
        return
    
    def freq_start_check(self):
        """
        """
        self.freq_start = self._freq_start_check()
        return self.freq_start
    
    def freq_start_set(self, freq, unit='MHz'):
        """
        """
        self._freq_start_set(freq, unit)
        self.refresh()
        return
    
    def freq_stop_check(self):
        """
        """
        self.freq_stop = self._freq_stop_check()
        return self.freq_stop
    
    def freq_stop_set(self, freq, unit='MHz'):
        """
        """
        self._freq_stop_set(freq, unit)
        self.refresh()
        return
    
    def freq_span_check(self):
        """
        """
        self.freq_span = self._freq_span_check()
        return self.freq_span
    
    def freq_span_set(self, freq, unit='MHz'):
        """
        """
        self._freq_span_set(freq, unit)
        self.refresh()
        return
    
    def resolutionBW_check(self):
        """
        """
        self.resolutionBW = self._resolutionBW_check()
        return self.resolutionBW
    
    def resolutionBW_set(self, freq, unit='MHz'):
        """
        """
        self._resolutionBW_set(freq, unit)
        self.refresh()
        return
    
    def full_span_set(self, freq, unit='MHz'):
        """
        """
        self._full_span_set(freq, unit)
        self.refresh()
        return
    
    def zero_span_set(self, freq, unit='MHz'):
        """
        """
        self._zero_span_set(freq, unit)
        self.refresh()
        return
    
    def sweeppoints_check(self):
        """
        """
        self.sweeppoints = self._sweeppoints_check()
        return self.sweeppoints
    
    def sweeppoints_set(self, points):
        """
        """
        self._sweeppoints_set(points)
        self.refresh()
        return 
    
    def sweeptime_check(self):
        """
        """
        self.sweeptime = self._sweeptime_check()
        return self.sweeptime
    
    def sweeptime_set(self, msec):
        """
        """
        self._sweeptime_set(msec)
        self.refresh()
        return 
    
    def attenuation_check(self):
        """
        """
        self.attenuation = self._attenuation_check()
        return self.attenuation
    
    def attenuation_set(self, dB):
        """
        """
        self._attenuation_set(dB)
        self.refresh()
        return 
    
    def referencelevel_check(self):
        """
        """
        self.referencelevel = self._referencelevel_check()
        return self.referencelevel
    
    def referencelevel_set(self, dB):
        """
        """
        self._referencelevel_set(dB)
        self.refresh()
        return 
    
    def scaledivision_set(self, dB):
        """
        """
        self._scaledivision_set(dB)
        self.refresh()
        return 
    
    def videoBW_check(self):
        """
        """
        self.videoBW = self._videoBW_check()
        return self.videoBW
    
    def videoBW_set(self, freq, unit='MHz'):
        """
        """
        self._videoBW_set(freq, unit)
        self.refresh()
        return
    
    def average_check(self):
        """
        """
        self.average = self._average_check()
        return self.average
    
    def average_set(self, average):
        """
        """
        self._average_set(average)
        self.refresh()
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
        
        
        # measure
        # -------
        print('%-38s'%'measure():'),
        try:
            ret = self.measure()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            else: print('OK, [%.2f %.2f ... %.2f %.2f]'%(ret[0], ret[1], ret[-2], ret[-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # freq_center
        # -----------
        print('%-38s'%'freq_center_check():'),
        try:
            ret = self.freq_center_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"freq_center_set(100, 'MHz'):"),
        try:
            self.freq_center_set(100, 'MHz')
            wait()
            ret = self.freq_center_check()
            if ret!=100*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"freq_center_set(9.8765432101, 'GHz'):"),
        try:
            self.freq_center_set(9.8765432101, 'GHz')
            wait()
            ret = self.freq_center_check()
            if ret!=9.8765432101*1e9: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # freq_start
        # -----------
        print('%-38s'%'freq_start_check():'),
        try:
            ret = self.freq_start_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"freq_start_set(100, 'MHz'):"),
        try:
            self.freq_start_set(100, 'MHz')
            wait()
            ret = self.freq_start_check()
            if ret!=100*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"freq_start_set(9.8765432101, 'GHz'):"),
        try:
            self.freq_start_set(9.8765432101, 'GHz')
            wait()
            ret = self.freq_start_check()
            if ret!=9.8765432101*1e9: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # freq_stop
        # -----------
        print('%-38s'%'freq_stop_check():'),
        try:
            ret = self.freq_stop_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"freq_stop_set(100, 'MHz'):"),
        try:
            self.freq_stop_set(100, 'MHz')
            wait()
            ret = self.freq_stop_check()
            if ret!=100*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"freq_stop_set(9.8765432101, 'GHz'):"),
        try:
            self.freq_stop_set(9.8765432101, 'GHz')
            wait()
            ret = self.freq_stop_check()
            if ret!=9.8765432101*1e9: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # freq_span
        # -----------
        print('%-38s'%'freq_span_check():'),
        try:
            ret = self.freq_span_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"freq_span_set(100, 'MHz'):"),
        try:
            self.freq_span_set(100, 'MHz')
            wait()
            ret = self.freq_span_check()
            if ret!=100*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"freq_span_set(1.2345678901, 'GHz'):"),
        try:
            self.freq_span_set(1.2345678901, 'GHz')
            wait()
            ret = self.freq_span_check()
            if ret!=1.2345678901*1e9: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # resolutionBW
        # ------------
        print('%-38s'%'resolutionBW_check():'),
        try:
            ret = self.resolutionBW_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"resolutionBW_set(1, 'MHz'):"),
        try:
            self.resolutionBW_set(1, 'MHz')
            wait()
            ret = self.resolutionBW_check()
            if ret!=1*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"resolutionBW_set(100, 'kHz'):"),
        try:
            self.resolutionBW_set(100, 'kHz')
            wait()
            ret = self.resolutionBW_check()
            if ret!=100*1e3: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        # full_span
        # ---------
        print('%-38s'%"full_span_set(1000, 'MHz'):"),
        try:
            self.full_span_set(1000, 'MHz')
            wait()
            print('OK, *** to be implemented ***')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        # zero_span
        # ---------
        print('%-38s'%"zero_span_set(1000, 'MHz'):"),
        try:
            self.zero_span_set(1000, 'MHz')
            wait()
            print('OK, *** to be implemented ***')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        # sweeppoints
        # -----------
        print('%-38s'%'sweeppoints_check():'),
        try:
            ret = self.sweeppoints_check()
            if type(ret)!=int: print('!! Bad !!, return is not float')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"sweeppoints_set(1001):"),
        try:
            self.sweeppoints_set(1001)
            wait()
            ret = self.sweeppoints_check()
            if ret!=1001: print('!! Bad !!, %f'%(ret))
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # sweeptime
        # ---------
        print('%-38s'%'sweeptime_check():'),
        try:
            ret = self.sweeptime_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"sweeptime_set(100):"),
        try:
            self.sweeptime_set(100)
            wait()
            ret = self.sweeptime_check()
            if ret!=100.0: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # attenuation
        # -----------
        print('%-38s'%'attenuation_check():'),
        try:
            ret = self.attenuation_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"attenuation_set(10.0):"),
        try:
            self.attenuation_set(10.0)
            wait()
            ret = self.attenuation_check()
            if ret!=10.0: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        # referencelevel
        # --------------
        print('%-38s'%'referencelevel_check():'),
        try:
            ret = self.referencelevel_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"referencelevel_set(5.0):"),
        try:
            self.referencelevel_set(5.0)
            wait()
            ret = self.referencelevel_check()
            if ret!=5.0: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass            
        
        # scaledivision
        # -------------
        print('%-38s'%"scaledivision_set(5):"),
        try:
            self.scaledivision_set(5)
            wait()
            print('OK, *** to be implemented ***')
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        # videoBW
        # -------
        print('%-38s'%'videoBW_check():'),
        try:
            ret = self.videoBW_check()
            if type(ret)!=float: print('!! Bad !!, return is not float')
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"videoBW_set(1, 'MHz'):"),
        try:
            self.videoBW_set(1, 'MHz')
            wait()
            ret = self.videoBW_check()
            if ret!=1*1e6: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        print('%-38s'%"videoBW_set(100, 'kHz'):"),
        try:
            self.videoBW_set(100, 'kHz')
            wait()
            ret = self.videoBW_check()
            if ret!=100*1e3: print('!! Bad !!, %f'%(ret))
            else: print('OK, %f'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        # average
        # -------
        print('%-38s'%'average_check():'),
        try:
            ret = self.average_check()
            if type(ret)!=int: print('!! Bad !!, return is not float')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        print('%-38s'%"average_set(20):"),
        try:
            self.average_set(20)
            wait()
            ret = self.average_check()
            if ret!=20: print('!! Bad !!, %f'%(ret))
            else: print('OK, %d'%ret)
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
    
    def _freq_center_check(self):
        return float()
    
    def _freq_center_set(self, freq, unit):
        return None
    
    def _freq_start_check(self):
        return float()
    
    def _freq_start_set(self, freq, unit):
        return None
    
    def _freq_stop_check(self):
        return float()
    
    def _freq_stop_set(self, freq, unit):
        return None
    
    def _freq_span_check(self):
        return float()
    
    def _freq_span_set(self, freq, unit):
        return None
    
    def _resolutionBW_check(self):
        return float()
    
    def _resolutionBW_set(self, freq, unit):
        return None
    
    def _full_span_set(self, freq, unit):
        return None
    
    def _zero_span_set(self, freq, unit):
        return None
    
    def _sweeppoints_check(self):
        return int()
    
    def _sweeppoints_set(self, points):
        return None
    
    def _sweeptime_check(self):
        return float()
    
    def _sweeptime_set(self, msec):
        return None
    
    def _attenuation_check(self):
        return float()
    
    def _attenuation_set(self, dB):
        return None
    
    def _referencelevel_check(self):
        return float()
    
    def _referencelevel_set(self, dB):
        return None
    
    def _scaledivision_set(self, dB):
        return None
    
    def _videoBW_check(self):
        return float()
    
    def _videoBW_set(self, freq, unit):
        return None
    
    def _average_check(self):
        return int()
    
    def _average_set(self, average):
        return None
    
    def _model_check(self):
        return str()
        
    def _preset(self):
        return None



# ===================
# Dummy Server/Client
# ===================
dummy_api = {'measure': 'dummy_sa:measure',
             'freq_center_check': 'dummy_sa:freq_center_check',
             'freq_center_set': 'dummy_sa:freq_center_set',
             'freq_start_check': 'dummy_sa:freq_start_check',
             'freq_start_set': 'dummy_sa:freq_start_set',
             'freq_stop_check': 'dummy_sa:freq_stop_check',
             'freq_stop_set': 'dummy_sa:freq_stop_set',
             'freq_span_check': 'dummy_sa:freq_span_check',
             'freq_span_set': 'dummy_sa:freq_span_set',
             'resolutionBW_check': 'dummy_sa:resolutionBW_check',
             'resolutionBW_set': 'dummy_sa:resolutionBW_set',
             'full_span_set': 'dummy_sa:full_span_set',
             'zero_span_set': 'dummy_sa:zero_span_set',
             'sweeppoints_check': 'dummy_sa:sweeppoints_check',
             'sweeppoints_set': 'dummy_sa:sweeppoints_set',
             'sweeptime_check': 'dummy_sa:sweeptime_check',
             'sweeptime_set': 'dummy_sa:sweeptime_set',
             'attenuation_check': 'dummy_sa:attenuation_check',
             'attenuation_set': 'dummy_sa:attenuation_set',
             'referencelevel_check': 'dummy_sa:referencelevel_check',
             'referencelevel_set': 'dummy_sa:referencelevel_set',
             'scaledivision_set': 'dummy_sa:scaledivision_set',
             'videoBW_check': 'dummy_sa:videoBW_check',
             'videoBW_set': 'dummy_sa:videoBW_set',
             'average_check': 'dummy_sa:average_check',
             'average_set': 'dummy_sa:average_set'}

# dummy client
# ============
class dummy_client(spectrumanalyzer):
    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        spectrumanalyzer.__init__(self, com)
        pass
        
    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return
        
    def _measure(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['measure']))
        time.sleep(0.05)
        spectrum = map(float, self.com.readline().split(' '))
        self.com.close()
        return spectrum
    
    def _freq_center_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['freq_center_check']))
        freq = float(self.com.readline())
        self.com.close()
        return freq
        
    def _freq_center_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %.10f %s\n'%(dummy_api['freq_center_set'], freq, unit))
        self.com.close()
        return 
        
    def _freq_start_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['freq_start_check']))
        freq = float(self.com.readline())
        self.com.close()
        return freq
        
    def _freq_start_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %.10f %s\n'%(dummy_api['freq_start_set'], freq, unit))
        self.com.close()
        return 
        
    def _freq_stop_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['freq_stop_check']))
        freq = float(self.com.readline())
        self.com.close()
        return freq
        
    def _freq_stop_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %.10f %s\n'%(dummy_api['freq_stop_set'], freq, unit))
        self.com.close()
        return 
        
    def _freq_span_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['freq_span_check']))
        freq = float(self.com.readline())
        self.com.close()
        return freq
        
    def _freq_span_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %.10f %s\n'%(dummy_api['freq_span_set'], freq, unit))
        self.com.close()
        return 
        
    def _resolutionBW_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['resolutionBW_check']))
        bw = float(self.com.readline())
        self.com.close()
        return bw
        
    def _resolutionBW_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(dummy_api['resolutionBW_set'], freq, unit))
        self.com.close()
        return 
        
    def _full_span_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(dummy_api['full_span_set'], freq, unit))
        self.com.close()
        return 
        
    def _zero_span_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(dummy_api['zero_span_set'], freq, unit))
        self.com.close()
        return 
        
    def _sweeppoints_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['sweeppoints_check']))
        points = int(self.com.readline())
        self.com.close()
        return points
        
    def _sweeppoints_set(self, points):
        self.com.open()
        self.com.send('%s %d\n'%(dummy_api['sweeppoints_set'], points))
        self.com.close()
        return 

    def _sweeptime_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['sweeptime_check']))
        sweeptime = float(self.com.readline())
        self.com.close()
        return sweeptime
        
    def _sweeptime_set(self, msec):
        self.com.open()
        self.com.send('%s %f\n'%(dummy_api['sweeptime_set'], msec))
        self.com.close()
        return 

    def _attenuation_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['attenuation_check']))
        attenuation = float(self.com.readline())
        self.com.close()
        return attenuation
        
    def _attenuation_set(self, dB):
        self.com.open()
        self.com.send('%s %f\n'%(dummy_api['attenuation_set'], dB))
        self.com.close()
        return 

    def _referencelevel_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['referencelevel_check']))
        referencelevel = float(self.com.readline())
        self.com.close()
        return referencelevel
        
    def _referencelevel_set(self, dB):
        self.com.open()
        self.com.send('%s %f\n'%(dummy_api['referencelevel_set'], dB))
        self.com.close()
        return 
        
    def _scaledivision_set(self, dB):
        self.com.open()
        self.com.send('%s %f\n'%(dummy_api['scaledivision_set'], dB))
        self.com.close()
        return 
        
    def _videoBW_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['videoBW_check']))
        videoBW = float(self.com.readline())
        self.com.close()
        return videoBW
        
    def _videoBW_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(dummy_api['videoBW_set'], freq, unit))
        self.com.close()
        return 
        
    def _average_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['average_check']))
        average = int(self.com.readline())
        self.com.close()
        return average
        
    def _average_set(self, average):
        self.com.open()
        self.com.send('%s %d\n'%(dummy_api['average_set'], average))
        self.com.close()
        return 
        
    def _model_check(self):
        return 'SpectrumAnalyzer_Dummy'


# dummy server
# ============
class dummy_server(object):
    freq_center = 1e9
    freq_start = 0
    freq_stop = 2e9
    freq_span = 2e9
    full_span = None
    zero_span = None
    sweeppoints = 401
    sweeptime = 500   # msec
    attenuation = 0
    referencelevel = 0
    scaledivision = 10
    average = 1
    resolutionBW = 3e6
    videoBW = 10e3
    
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
        if command==dummy_api['measure']: self.measure(params)
        elif command==dummy_api['freq_center_check']: self.freq_center_check(params)
        elif command==dummy_api['freq_center_set']: self.freq_center_set(params)
        elif command==dummy_api['freq_start_check']: self.freq_start_check(params)
        elif command==dummy_api['freq_start_set']: self.freq_start_set(params)
        elif command==dummy_api['freq_stop_check']: self.freq_stop_check(params)
        elif command==dummy_api['freq_stop_set']: self.freq_stop_set(params)
        elif command==dummy_api['freq_span_check']: self.freq_span_check(params)
        elif command==dummy_api['freq_span_set']: self.freq_span_set(params)
        elif command==dummy_api['resolutionBW_check']: self.resolutionBW_check(params)
        elif command==dummy_api['resolutionBW_set']: self.resolutionBW_set(params)
        elif command==dummy_api['full_span_set']: self.full_span_set(params)
        elif command==dummy_api['zero_span_set']: self.zero_span_set(params)
        elif command==dummy_api['sweeppoints_check']: self.sweeppoints_check(params)
        elif command==dummy_api['sweeppoints_set']: self.sweeppoints_set(params)
        elif command==dummy_api['sweeptime_check']: self.sweeptime_check(params)
        elif command==dummy_api['sweeptime_set']: self.sweeptime_set(params)
        elif command==dummy_api['attenuation_check']: self.attenuation_check(params)
        elif command==dummy_api['attenuation_set']: self.attenuation_set(params)
        elif command==dummy_api['referencelevel_check']: self.referencelevel_check(params)
        elif command==dummy_api['referencelevel_set']: self.referencelevel_set(params)
        elif command==dummy_api['scaledivision_set']: self.scaledivision_set(params)
        elif command==dummy_api['videoBW_check']: self.videoBW_check(params)
        elif command==dummy_api['videoBW_set']: self.videoBW_set(params)
        elif command==dummy_api['average_check']: self.average_check(params)
        elif command==dummy_api['average_set']: self.average_set(params)
        else: print(command, params)
        return
        
    def measure(self, params):
        base = random.randrange(100, 1200)
        spectrum = [random.random()*base/10.+base for i in range(self.sweeppoints)]
        ret = ' '.join(map(str, spectrum))
        self.client.send('%s\n'%(ret))
        return
        
    def freq_center_check(self, params):
        self.client.send('%.10f\n'%(self.freq_center))
        return
        
    def freq_center_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.freq_center = freq
        self.freq_start = freq - self.freq_span/2.
        self.freq_stop = freq + self.freq_span/2.
        return
        
    def freq_start_check(self, params):
        self.client.send('%.10f\n'%(self.freq_start))
        return
        
    def freq_start_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.freq_start = freq
        self.freq_center = (self.freq_start + self.freq_stop)/2.
        self.freq_span = self.freq_stop - self.freq_start
        return
        
    def freq_stop_check(self, params):
        self.client.send('%.10f\n'%(self.freq_stop))
        return
        
    def freq_stop_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.freq_stop = freq
        self.freq_center = (self.freq_start + self.freq_stop)/2.
        self.freq_span = self.freq_stop - self.freq_start
        return
        
    def freq_span_check(self, params):
        self.client.send('%.10f\n'%(self.freq_span))
        return
        
    def freq_span_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.freq_span = freq
        self.freq_start = self.freq_center - self.freq_span/2.
        self.freq_stop = self.freq_center + self.freq_span/2.
        return
        
    def resolutionBW_check(self, params):
        self.client.send('%.10f\n'%(self.resolutionBW))
        return
        
    def resolutionBW_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.resolutionBW = freq
        return
        
    def full_span_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.full_span = freq
        return
        
    def zero_span_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.zero_span = freq
        return
        
    def sweeppoints_check(self, params):
        self.client.send('%d\n'%(self.sweeppoints))
        return
        
    def sweeppoints_set(self, params):
        points = int(params[0])
        self.sweeppoints = points
        return
        
    def sweeptime_check(self, params):
        self.client.send('%f\n'%(self.sweeptime))
        return
        
    def sweeptime_set(self, params):
        sweeptime = float(params[0])
        self.sweeptime = sweeptime
        return
        
    def attenuation_check(self, params):
        self.client.send('%f\n'%(self.attenuation))
        return
        
    def attenuation_set(self, params):
        attenuation = float(params[0])
        self.attenuation = attenuation
        return
        
    def referencelevel_check(self, params):
        self.client.send('%f\n'%(self.referencelevel))
        return
        
    def referencelevel_set(self, params):
        level = float(params[0])
        self.referencelevel = level
        return
        
    def scaledivision_set(self, params):
        scale = float(params[0])
        self.scaledivision = scale
        return
        
    def videoBW_check(self, params):
        self.client.send('%.10f\n'%(self.videoBW))
        return
        
    def videoBW_set(self, params):
        freq = float(params[0]) * self.freq_unit[params[1].lower()]
        self.videoBW = freq
        return
        
    def average_check(self, params):
        self.client.send('%d\n'%(self.average))
        return

    def average_set(self, params):
        average = int(params[0])
        self.average = average
        return
        
        

        
    
