#! /usr/bin/env python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))

import device

class signalgenerator(device.device):
    freq_unit = {'hz': 1, 'khz': 1e3, 'mhz': 1e6, 'ghz': 1e9}
    api = {'freq_set': '',
           'freq_check': '',
           'power_set': '',
           'power_check': '',
           'output_on': '',
           'output_off': '',
           'output_check': ''}
    freq = None
    power = None
    output = None
    
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
        
    def power_set(self, power, unit='DBm'):
        """
        """
        self._power_set(power)
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
        
    def _freq_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(self.api['freq_set'], freq, unit))
        self.com.close()
        return
    
    def _freq_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['freq_check']))
        freq = float(self.com.readline())
        self.com.close()
        if abs(freq - self.freq)>1e-3: assert Error
        return freq
        
    def _power_set(self, power, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(self.api['power_set'], power, unit))
        self.com.close()
        return
    
    def _power_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['power_set']))
        power = float(self.com.readline())
        self.com.close()
        if abs(power - self.power)>1e-3: assert Error
        return power
        
    def _output_on(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_on']))
        self.com.close()
        return
        
    def _output_off(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_off']))
        self.com.close()
        return        
    
    def _output_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_check']))
        output = int(self.com.readline())
        self.com.close()
        if output!=self.output: assert Error
        return output
        
    
class dummy(signalgenerator):
    def _freq_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(self.api['freq_set'], freq, unit))
        self.com.close()
        return
    
    def _freq_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['freq_check']))
        self.com.close()
        return self.freq
        
    def _power_set(self, power, unit):
        self.com.open()
        self.com.send('%s %f %s\n'%(self.api['power_set'], power, unit))
        self.com.close()
        return
    
    def _power_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['power_set']))
        self.com.close()
        return self.power
        
    def _output_on(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_on']))
        self.com.close()
        return
        
    def _output_off(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_off']))
        self.com.close()
        return        
    
    def _output_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_check']))
        self.com.close()
        return self.output
    
