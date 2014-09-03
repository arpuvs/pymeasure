#! /usr/bin/env python

import os
import sys
import time
import threading
import socket
import random

from .. import device


# ===============
# Interface Class
# ===============
class daq(device.device):
    # property configuration
    # ======================
    ad_num = 0
    da_num = 0
    dio_num = 0
    
    # constructor
    # ===========
    def __init__(self, com=None):
        device.device.__init__(self, com)
        self.model_check()
        self.ad_chnum_check()
        self.da_chnum_check()
        self.dio_chnum_check()
        pass
    
    # method
    # ======
    def _create_value_ch_pair(self, val, ch, chnum):
        if ch is None: ch = [i+1 for i in range(chnum)]
        if type(val) not in [list, tuple]:
            val = [val for i in range(len(ch))]
            pass
        return val, ch
    
    # interface method
    # ================
    def ad_chnum_check(self):
        self.ad_num = self._ad_chnum_check()
        return self.ad_num
    
    def ad_measure(self, repeat=1, integ=0, start=0):
        """
        """
        if start<time.time(): start = time.time()
        if integ==0: integ = 0.01 ###
        ad = self._ad_measure(repeat, integ, start)
        return ad
    
    def ad_capability_check(self):
        res = self.ad_resolution_capability_check()
        samp = self.ad_sampling_capability_check()
        vrange = self.ad_range_capability_check()
        return res, samp, vrange
    
    def ad_config_check(self):
        """
        """
        res = self.ad_resolution_check()
        samp = self.ad_sampling_check()
        vrange = self.ad_range_check()
        return res, samp, vrange
    
    def ad_resolution_capability_check(self):
        """
        """
        res_cap = self._ad_resolution_capability_check()
        return res_cap
        
    def ad_resolution_check(self):
        """
        """
        res = self._ad_resolution_check()
        return res
        
    def ad_resolution_set(self, bit):
        """
        """
        self._ad_resolution_set(bit)
        return
        
    def ad_sampling_capability_check(self):
        """
        """
        sampling_cap = self._ad_sampling_capability_check()
        return sampling_cap
        
    def ad_sampling_check(self):
        """
        """
        sampling = self._ad_sampling_check()
        return sampling
        
    def ad_sampling_set(self, sampling):
        """
        """
        self._ad_sampling_set(sampling)
        return
        
    def ad_range_capability_check(self):
        """
        """
        vrange_cap = self._ad_range_capability_check()
        return vrange_cap
        
    def ad_range_check(self):
        """
        """
        vrange = self._ad_range_check()
        return vrange
        
    def ad_range_set(self, vrange):
        """
        """
        self._ad_range_set(vrange)
        return
         
    def da_chnum_check(self):
        self.da_num = self._da_chnum_check()
        return self.da_num
    
    def da_check(self):
        """
        """
        da = self._da_check()
        return da
    
    def da_set(self, bias, ch=None):
        """
        """
        bias, ch = self._create_value_ch_pair(bias, ch, self.da_num)
        self._da_set(bias, ch)
        return None
    
    def da_series_set(self):
        pass
        
    def da_range_capability_check(self):
        """
        """
        vrange_cap = self._da_range_capability_check()
        return vrange_cap
        
    def da_range_check(self):
        """
        """
        vrange = self._da_range_check()
        return vrange
        
    def da_range_set(self, vrange):
        """
        """
        self._da_range_set(vrange)
        return
    
    def dio_chnum_check(self):
        self.dio_num = self._dio_chnum_check()
        return self.dio_num
    
    def dio_check(self, repeat=1, interval=0.01, start=0):
        """
        """
        dio = self._dio_check(repeat, interval, start)
        return dio
        
    def dio_set(self, dio, ch=None):
        """
        """
        dio, ch = self._create_value_ch_pair(dio, ch, self.dio_num)
        self._dio_set(dio, ch)
        return None
    
    def model_check(self):
        self.model = self._model_check()
        return self.model
        
    def preset(self):
        self._preset()
        return 
    
    # self test
    # =========
    def self_test(self, interval=0.2):
        wait = lambda: time.sleep(interval)
        
        print('self_tset :: daq')
        print('============================')
        print('model: %s'%(self.model))
        print('communicator: %s'%(self.com.method))
        print('----------------------------')
        
        print('initialize')
        print('----------')
        print('preset()')
        self.preset()
        
        print('')
        print('test start')
        print('----------')
        
        wait()
        print('%-35s'%'ad_chnum_check():'),
        try:
            ret = self.ad_chnum_check()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            elif ret<0: print('!! Bad !!, return is smaller than -1')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'da_chnum_check():'),
        try:
            ret = self.da_chnum_check()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            elif ret<0: print('!! Bad !!, return is smaller than -1')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'dio_chnum_check():'),
        try:
            ret = self.dio_chnum_check()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            elif ret<0: print('!! Bad !!, return is smaller than -1')
            else: print('OK, %d'%ret)
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_measure(1, 0, 0):'),
        try:
            ret = self.ad_measure(1, 0, 0)
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)!=1: print('!! Bad !!, return has %d shots, not 1'%len(ret))
            elif len(ret[0])!=self.ad_num: print('!! Bad !!, return has %d ch, not %d'%
                                                 (len(ret[0]), self.ad_num))
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0][0], ret[0][1],
                                                         ret[0][-2], ret[0][-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        now = time.time()
        print('%-35s'%'ad_measure(5, 0.1, 0):'),
        try:
            ret = self.ad_measure(5, 0.1, 0)
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)!=5: print('!! Bad !!, return has %d shots, not 5'%len(ret))
            elif len(ret[0])!=self.ad_num: print('!! Bad !!, return has %d ch, not %d'%
                                                 (len(ret[0]), self.ad_num))
            elif now>(time.time()-0.5): print('!! Bad !!, return comes too quick')
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0][0], ret[0][1],
                                                         ret[0][-2], ret[0][-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        now = time.time()
        print('%-35s'%'ad_measure(10, 0.05, now+1):'),
        try:
            ret = self.ad_measure(10, 0.05, now+1)
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)!=10: print('!! Bad !!, return has %d shots, not 10'%len(ret))
            elif len(ret[0])!=self.ad_num: print('!! Bad !!, return has %d ch, not %d'%
                                                 (len(ret[0]), self.ad_num))
            elif now>(time.time()-1): print('!! Bad !!, return comes too quick')
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0][0], ret[0][1],
                                                         ret[0][-2], ret[0][-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_capability_check():'),
        try:
            ret = self.ad_capability_check()
            res = self.ad_resolution_capability_check()
            samp = self.ad_sampling_capability_check()
            vrange = self.ad_range_capability_check()
            if type(ret)!=tuple: print('!! Bad !!, return is not tuple')
            elif ret[0]!=res: print('!! Bad !!, ret[0] is not resolutions')
            elif ret[1]!=samp: print('!! Bad !!, ret[1] is not samples')
            elif ret[2]!=vrange: print('!! Bad !!, ret[2] is not vranges')
            else: print('OK, [[%d ...] [%s ...] [%s ...]]'%(ret[0][0], ret[1][0], ret[2][0]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
                        
        wait()
        print('%-35s'%'ad_resolution_capability_check():'),
        try:
            ret = self.ad_resolution_capability_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [int==type(d) for d in ret]: print('!! Bad !!, returns must be int')
            elif 0 in ret: print('!! Bad !!, returns must not be 0')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
                        
        wait()
        print('%-35s'%'ad_sampling_capability_check():'),
        try:
            ret = self.ad_sampling_capability_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [int==type(d) for d in ret]: print('!! Bad !!, returns must be int')
            elif 0 in ret: print('!! Bad !!, returns must not be 0')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
                        
        wait()
        print('%-35s'%'ad_range_capability_check():'),
        try:
            ret = self.ad_range_capability_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [list==type(d) for d in ret]: print('!! Bad !!, returns must be list')
            elif False in [float==type(d) for d in ret[0]]: print('!! Bad !!, range must be float')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_resolution_check():'),
        try:
            ret = self.ad_resolution_check()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            elif ret<1: print('!! Bad !!, return must be >1')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_resolution_set(12):'),
        try:
            self.ad_resolution_set(12)
            wait()
            res = self.ad_resolution_check()
            resc = self.ad_resolution_capability_check()
            if 12 in resc:
                if res!=12: print('!! Bad !!, %d'%(res))
                else: print('OK, %s'%(res))
            else:
                if res==12: print('!! Bad !!, %d'%(res))
                else: print('OK, %s'%(res))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'ad_resolution_set(11):'),
        try:
            self.ad_resolution_set(11)
            wait()
            res = self.ad_resolution_check()
            resc = self.ad_resolution_capability_check()
            if 11 in resc:
                if res!=11: print('!! Bad !!, %d'%(res))
                else: print('OK, %s'%(res))
            else:
                if res==11: print('!! Bad !!, %d'%(res))
                else: print('OK, %s'%(res))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'ad_sampling_check():'),
        try:
            ret = self.ad_sampling_check()
            if type(ret)!=int: print('!! Bad !!, return is not int')
            elif ret<1: print('!! Bad !!, return must be >1')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_sampling_set(1000):'),
        try:
            setsamp = 1000
            self.ad_sampling_set(setsamp)
            wait()
            samp = self.ad_sampling_check()
            sampc = self.ad_sampling_capability_check()
            if setsamp in sampc:
                if samp!=setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
            else:
                if samp==setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'ad_sampling_set(2000):'),
        try:
            setsamp = 2000
            self.ad_sampling_set(setsamp)
            wait()
            samp = self.ad_sampling_check()
            sampc = self.ad_sampling_capability_check()
            if setsamp in sampc:
                if samp!=setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
            else:
                if samp==setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'ad_sampling_set(500000):'),
        try:
            setsamp = 500000
            self.ad_sampling_set(setsamp)
            wait()
            samp = self.ad_sampling_check()
            sampc = self.ad_sampling_capability_check()
            if setsamp in sampc:
                if samp!=setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
            else:
                if samp==setsamp: print('!! Bad !!, %d'%(samp))
                else: print('OK, %s'%(samp))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_range_check():'),
        try:
            ret = self.ad_range_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [float==type(d) for d in ret]: print('!! Bad !!, range must be float')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'ad_range_set(ad_range_cap[0]):'),
        try:
            setrange = self.ad_range_capability_check()[0]
            self.ad_range_set(setrange)
            wait()
            ret = self.ad_range_check()
            if ret!=setrange: print('!! Bad !!, %s'%(ret))
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'ad_range_set([0, 3]):'),
        try:
            setrange = [0, 3]
            self.ad_range_set(setrange)
            wait()
            ret = self.ad_range_check()
            cap = self.ad_range_capability_check()
            if setrange in cap:
                if ret!=setrange: print('!! Bad !!, %s'%(ret))
                else: print('OK, %s'%(ret))
            else:
                if ret==setrange: print('!! Bad !!, %s'%(ret))
                else: print('OK, %s'%(ret))
                pass
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'da_check():'),
        try:
            ret = self.da_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [float==type(d) for d in ret]: print('!! Bad !!, range must be float')
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0], ret[1], ret[-2], ret[-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'da_set(0.0):'),
        try:
            self.da_set(0.0)
            wait()
            ret = self.da_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif False in [0==d for d in ret]: print('!! Bad !!, return is not 0')
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0], ret[1], ret[-2], ret[-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'da_set([0.1, 0], [1, 2]):'),
        try:
            self.da_set([0.1, 0.0], [1, 2])
            wait()
            ret = self.da_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif ret[0]!=0.1: print('!! Bad !!, ret[0] is not 0.1')
            elif ret[1]!=0: print('!! Bad !!, ret[1] is not 0')
            else: print('OK, [%.1f %.1f ... %.1f %.1f]'%(ret[0], ret[1], ret[-2], ret[-1]))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'da_range_capability_check():'),
        try:
            ret = self.da_range_capability_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [list==type(d) for d in ret]: print('!! Bad !!, returns must be list')
            elif False in [float==type(d) for d in ret[0]]: print('!! Bad !!, range must be float')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass

        wait()
        print('%-35s'%'da_range_check():'),
        try:
            ret = self.da_range_check()
            if type(ret)!=list: print('!! Bad !!, return is not list')
            elif len(ret)<1: print('!! Bad !!, return no parameters')
            elif False in [float==type(d) for d in ret]: print('!! Bad !!, range must be float')
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
        
        wait()
        print('%-35s'%'da_range_set(ad_range_cap[0]):'),
        try:
            setrange = self.da_range_capability_check()[0]
            self.da_range_set(setrange)
            wait()
            ret = self.da_range_check()
            if ret!=setrange: print('!! Bad !!, %s'%(ret))
            else: print('OK, %s'%(ret))
        except:
            err = sys.exc_info()
            print('!! Error !!, %s, %s'%(err[0].__name__, err[1]))
            pass
            
        wait()
        print('%-35s'%'da_range_set([0, 1]):'),
        try:
            setrange = [0, 1]
            self.da_range_set(setrange)
            wait()
            ret = self.da_range_check()
            cap = self.da_range_capability_check()
            if setrange in cap:
                if ret!=setrange: print('!! Bad !!, %s'%(ret))
                else: print('OK, %s'%(ret))
            else:
                if ret==setrange: print('!! Bad !!, %s'%(ret))
                else: print('OK, %s'%(ret))
                pass
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
    def _ad_chnum_check(self):
        return int()
        
    def _ad_measure(self, repeat, integ, start):
        return list(list((float(),)),)

    def _ad_resolution_capability_check(self):
        return list((int(),))

    def _ad_resolution_check(self):
        return int()
    
    def _ad_resolution_set(self, bit):
        return None
        
    def _ad_sampling_capability_check(self):
        return list((int(),))

    def _ad_sampling_check(self):
        return int()
    
    def _ad_sampling_set(self, sampling):
        return None
        
    def _ad_range_capability_check(self):
        return list(list((float(),float())),)
        
    def _ad_range_check(self):
        return list(float(),float())
    
    def _ad_range_set(self, vrange):
        return None
    
    def _da_check(self):
        return list(float(),)
        
    def _da_set(self, bias, ch):
        return None
    
    def _da_series_set(self):
        pass
        
    def _da_range_capability_check(self):
        return list(list((float(),float())),)
    
    def _da_range_check(self):
        return list(float(),float())
    
    def _da_range_set(self, vrange):
        return None
        
    def _dio_check(self, repeat, interval, start):
        return list(list(int(),),)
        
    def _dio_set(self, dio, ch):
        return None
        
    def _model_check(self):
        return str()
        
    def _preset(self):
        return None

        
# ===================
# Dummy Server/Client
# ===================
dummy_api = {'ad_chnum_check': 'dummy_daq:ad_chnum_check',
             'ad_measure': 'dummy_daq:ad_measure',
             'ad_resolution_capability_check': 'dummy_daq:ad_resolution_capability_check',
             'ad_resolution_check': 'dummy_daq:ad_resolution_check',
             'ad_resolution_set': 'dummy_daq:ad_resolution_set',
             'ad_sampling_capability_check': 'dummy_daq:ad_sampling_capability_check',
             'ad_sampling_check': 'dummy_daq:ad_sampling_check',
             'ad_sampling_set': 'dummy_daq:ad_sampling_set',
             'ad_range_capability_check': 'dummy_daq:ad_range_capability_check',
             'ad_range_check': 'dummy_daq:ad_range_check',
             'ad_range_set': 'dummy_daq:ad_range_set',
             'da_chnum_check': 'dummy_daq:da_chnum_check',
             'da_check': 'dummy_daq:da_check',
             'da_set': 'dummy_daq:da_set',
             'da_series_set': 'dummy_daq:da_series_set',
             'da_range_capability_check': 'dummy_daq:da_range_capability_check',
             'da_range_check': 'dummy_daq:da_range_check',
             'da_range_set': 'dummy_daq:da_range_set',
             'dio_chnum_check': 'dummy_daq:dio_chnum_check',
             'dio_check': 'dummy_daq:dio_check',
             'dio_set': 'dummy_daq:dio_set',
             'model_check': 'dummy_daq:model_check',
             'preset': 'dummy_daq:preset'}

# dummy client
# ============
class dummy_client(daq):
    def __init__(self, com):
        self.server = dummy_server(com.port)
        time.sleep(0.05)
        daq.__init__(self, com)
        pass
        
    def _wait(self, until):
        while True:
            if time.time()>=until: break
            time.sleep(0.01)
            continue
        return
        
    def server_stop(self):
        self.com.open()
        self.com.send('stop\n')
        self.com.close()
        return
        
    def _model_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['model_check']))
        model = self.com.readline().strip()
        self.com.close()
        return model
        
    def _preset(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['preset']))
        self.com.close()
        return

    def _ad_chnum_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_chnum_check']))
        chnum = int(self.com.readline())
        self.com.close()
        return chnum
        
    def _ad_measure(self, repeat, integ, start):
        self.com.open()
        self.com.send('%s %d %.6f %.6f\n'%(dummy_api['ad_measure'], repeat, integ, start))
        
        data = []
        for i in range(repeat):
            start_to_recv = start + integ*(i+1) + 0.1
            self._wait(start_to_recv)
            ret_str = self.com.readline().strip()
            ret_list = [float(d) for d in ret_str.split(' ')]
            data.append(ret_list)
            continue
        
        self.com.close()
        return data
    
    def _ad_resolution_capability_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_resolution_capability_check']))
        ret = self.com.readline()
        self.com.close()
        resolutions = [int(d) for d in ret.split()]
        return resolutions
        
    def _ad_resolution_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_resolution_check']))
        resolution = int(self.com.readline())
        self.com.close()
        return resolution
        
    def _ad_resolution_set(self, bit):
        self.com.open()
        self.com.send('%s %d\n'%(dummy_api['ad_resolution_set'], bit))
        self.com.close()
        return 
        
    def _ad_sampling_capability_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_sampling_capability_check']))
        ret = self.com.readline()
        self.com.close()
        samplings = [int(d) for d in ret.split()]
        return samplings
        
    def _ad_sampling_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_sampling_check']))
        sampling = int(self.com.readline())
        self.com.close()
        return sampling
        
    def _ad_sampling_set(self, sampling):
        self.com.open()
        self.com.send('%s %d\n'%(dummy_api['ad_sampling_set'], sampling))
        self.com.close()
        return 
        
    def _ad_range_capability_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_range_capability_check']))
        ret = self.com.readline()
        self.com.close()
        vranges = [[float(dd) for dd in d.split(',')] for d in ret.split(';')]
        return vranges
        
    def _ad_range_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['ad_range_check']))
        ret = self.com.readline()
        vrange = [float(d) for d in ret.split(',')]
        self.com.close()
        return vrange
        
    def _ad_range_set(self, vrange):
        self.com.open()
        self.com.send('%s %f %f\n'%(dummy_api['ad_range_set'], vrange[0], vrange[1]))
        self.com.close()
        return 
        
    def _da_chnum_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['da_chnum_check']))
        chnum = int(self.com.readline())
        self.com.close()
        return chnum

    def _da_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['da_check']))
        da_str = self.com.readline().strip()
        da = [float(d) for d in da_str.split(' ')]
        self.com.close()
        return da
        
    def _da_set(self, bias, ch):
        self.com.open()
        pbias = ','.join(['%.5f'%d for d in bias])
        pch = ','.join(['%.5f'%d for d in ch])
        self.com.send('%s %s %s\n'%(dummy_api['da_set'], pbias, pch))
        self.com.close()
        return
    
    def _da_range_capability_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['da_range_capability_check']))
        ret = self.com.readline()
        self.com.close()
        vranges = [[float(dd) for dd in d.split(',')] for d in ret.split(';')]
        return vranges
        
    def _da_range_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['da_range_check']))
        ret = self.com.readline()
        vrange = [float(d) for d in ret.split(',')]
        self.com.close()
        return vrange
        
    def _da_range_set(self, vrange):
        self.com.open()
        self.com.send('%s %f %f\n'%(dummy_api['da_range_set'], vrange[0], vrange[1]))
        self.com.close()
        return 

    def _dio_chnum_check(self):
        self.com.open()
        self.com.send('%s\n'%(dummy_api['dio_chnum_check']))
        chnum = int(self.com.readline())
        self.com.close()
        return chnum

        
        

# dummy server
# ============
class dummy_server(object):
    ad_num = 64
    da_num = 32
    dio_num = 100
    
    ad_resolution_capability = [8, 12, 16] # bit
    ad_sampling_capability = [1000, 2000]
    ad_range_capability = [[-5, 5], [0, 5]]
    da_range_capability = [[0, 3], [0, 5]]
    
    ad_resolution = 16
    ad_sampling = 1000
    ad_range = [-5, 5]
    
    da = [i*0.05 for i in range(32)]
    da_range = [0, 5]
    
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
        if command==dummy_api['model_check']: self.model_check(params)
        elif command==dummy_api['preset']: self.preset(params)
        elif command==dummy_api['ad_chnum_check']: self.ad_chnum_check(params)
        elif command==dummy_api['ad_measure']: self.ad_measure(params)
        elif command==dummy_api['ad_resolution_capability_check']: self.ad_resolution_capability_check(params)
        elif command==dummy_api['ad_resolution_check']: self.ad_resolution_check(params)
        elif command==dummy_api['ad_resolution_set']: self.ad_resolution_set(params)
        elif command==dummy_api['ad_sampling_capability_check']: self.ad_sampling_capability_check(params)
        elif command==dummy_api['ad_sampling_check']: self.ad_sampling_check(params)
        elif command==dummy_api['ad_sampling_set']: self.ad_sampling_set(params)
        elif command==dummy_api['ad_range_capability_check']: self.ad_range_capability_check(params)
        elif command==dummy_api['ad_range_check']: self.ad_range_check(params)
        elif command==dummy_api['ad_range_set']: self.ad_range_set(params)
        elif command==dummy_api['da_chnum_check']: self.da_chnum_check(params)
        elif command==dummy_api['da_check']: self.da_check(params)
        elif command==dummy_api['da_set']: self.da_set(params)
        elif command==dummy_api['da_range_capability_check']: self.da_range_capability_check(params)
        elif command==dummy_api['da_range_check']: self.da_range_check(params)
        elif command==dummy_api['da_range_set']: self.da_range_set(params)
        elif command==dummy_api['dio_chnum_check']: self.dio_chnum_check(params)
        else: print(command, params)
        return
        
    def model_check(self, params):
        self.client.send('DAQ_Dummy\n')
        return
        
    def preset(self, params):
        return
        
    def ad_chnum_check(self, params):
        self.client.send('%d\n'%(self.ad_num))
        return
    
    def ad_measure(self, param):
        repeat = int(param[0])
        integ = float(param[1])
        start = float(param[2])
        
        for oneshot in range(repeat):
            dummy_data = [i+random.random() for i in range(self.ad_num)]
            dummy_str = ' '.join(['%.5f'%d for d in dummy_data])
            self.client.send(dummy_str+'\n')
            continue
        return
    
    def ad_resolution_capability_check(self, params):
        ret = ' '.join([str(d) for d in self.ad_resolution_capability])
        self.client.send(ret+'\n')
        return
        
    def ad_resolution_check(self, params):
        self.client.send('%d\n'%(self.ad_resolution))
        return
        
    def ad_resolution_set(self, params):
        newbit = int(params[0])
        if newbit in self.ad_resolution_capability:
            self.ad_resolution = newbit
            pass
        return
        
    def ad_sampling_capability_check(self, params):
        ret = ' '.join([str(d) for d in self.ad_sampling_capability])
        self.client.send(ret+'\n')
        return
        
    def ad_sampling_check(self, params):
        self.client.send('%d\n'%(self.ad_sampling))
        return
        
    def ad_sampling_set(self, params):
        newsampling = int(params[0])
        if newsampling in self.ad_sampling_capability:
            self.ad_sampling = newsampling
            pass
        return

    def ad_range_capability_check(self, params):
        ret = ';'.join(['%f,%f'%(d[0], d[1]) for d in self.ad_range_capability])
        self.client.send(ret+'\n')
        return
        
    def ad_range_check(self, params):
        vmin = self.ad_range[0]
        vmax = self.ad_range[1]
        self.client.send('%f,%f\n'%(vmin, vmax))
        return
        
    def ad_range_set(self, params):
        newvmin = float(params[0])
        newvmax = float(params[1])
        newrange = [newvmin, newvmax]
        if newrange in self.ad_range_capability:
            self.ad_range = newrange
            pass
        return

    def da_chnum_check(self, params):
        self.client.send('%d\n'%(self.da_num))
        return
        
    def da_check(self, params):
        retstr = ' '.join(['%.5f'%d for d in self.da])
        self.client.send('%s\n'%(retstr))
        return
        
    def da_set(self, params):
        bias = [float(d) for d in params[0].split(',')]
        ch = [int(float(d)) for d in params[1].split(',')]
        for b, c in zip(bias, ch):
            self.da[c-1] = b
            continue
        return
        
    def da_range_capability_check(self, params):
        ret = ';'.join(['%f,%f'%(d[0], d[1]) for d in self.da_range_capability])
        self.client.send(ret+'\n')
        return
        
    def da_range_check(self, params):
        vmin = self.da_range[0]
        vmax = self.da_range[1]
        self.client.send('%f,%f\n'%(vmin, vmax))
        return
        
    def da_range_set(self, params):
        newvmin = float(params[0])
        newvmax = float(params[1])
        newrange = [newvmin, newvmax]
        if newrange in self.da_range_capability:
            self.da_range = newrange
            pass
        return

    def dio_chnum_check(self, params):
        self.client.send('%d\n'%(self.dio_num))
        return
        
    
