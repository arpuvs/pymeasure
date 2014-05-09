#! /usr/bin/env python

import device

class signalgenerator(device.device):
    freq_unit = {'hz': 1, 'khz': 1e3, 'mhz': 1e6, 'ghz': 1e9}
    api = None
    freq = None
    power = None
    output = None
    
    def freq_set(self, freq, unit):
        """
        """
        self._freq_set(freq, unit)
        self.freq = freq * self.freq_unit[unit.lower()]
        return
    
    def _freq_set(self, freq, unit):
        self.com.open()
        self.com.send('%s %s %s\n'%(self.api['freq_set'], freq, unit))
        self.com.close()
        return
    
    def freq_check(self):
        """
        """
        self.freq = self._freq_check()
        return self.freq
        
    def _freq_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['freq_check']))
        freq = float(self.com.readline())
        self.com.close()
        if abs(freq - self.freq)>1e-3: assert Error
        return freq
        
    def power_set(self, power):
        """
        """
        self._power_set(power)
        self.power = power
        return
    
    def _power_set(self, power):
        self.com.open()
        self.com.send('%s %s\n'%(self.api['power_set'], power))
        self.com.close()
        return
    
    def power_check(self):
        """
        """
        self.power = self._power_check()
        return self.power
    
    def _power_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['power_set']))
        power = float(self.com.readline())
        self.com.close()
        if abs(power - self.power)>1e-3: assert Error
        return power
        
    def output_on(self):
        """
        """
        self._output_on()
        self.output = 1
        return
    
    def _output_on(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_on']))
        self.com.close()
        return
        
    def output_off(self):
        """
        """
        self._output_off()
        self.output = 0
        return
    
    def _output_off(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_off']))
        self.com.close()
        return        
    
    def output_check(self):
        """
        """
        self.output = self._output_check()
        return self.output
        
    def _output_check(self):
        self.com.open()
        self.com.send('%s\n'%(self.api['output_check']))
        output = int(self.com.readline())
        self.com.close()
        if output!=self.output: assert Error
        return output
        
    
    
