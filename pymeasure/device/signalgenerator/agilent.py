#! /usr/bin/env python

import signalgenerator as sg

class agilent(sg.signalgenerator):
    # internal method
    # ===============
    def _freq_set(self, freq, unit):
        self.com.open()
        self.com.send('FREQ %.10f %s\n'%(float(freq), unit))
        self.com.close()
        return
    
    def _freq_check(self):
        self.com.open()
        self.com.send('FREQ?\n')
        freq = float(self.com.readline())
        self.com.close()
        return freq
    
    def _power_set(self, power, unit):
        self.com.open()
        self.com.send('POW %f %s\n'%(float(power), unit))
        self.com.close()
        return 
    
    def _power_check(self):
        self.com.open()
        self.com.send('POW?\n')
        power = float(self.com.readline())
        self.com.close()
        return power
    
    def _output_on(self):
        self.com.open()
        self.com.send('OUTP 1\n')
        self.com.close()
        return

    def _output_off(self):
        self.com.open()
        self.com.send('OUTP 0\n')
        self.com.close()
        return
        
    def _output_check(self):
        self.com.open()
        self.com.send('OUTP?\n')
        outp = int(self.com.readline())
        self.com.close()
        return outp
        
    def _model_check(self):
        self.com.open()
        self.com.send('*IDN?\n')
        info = self.com.readline().strip()
        self.com.close()
        return info
        
    def preset(self):
        self.com.open()
        self.com.send('*RST\n')
        self.com.close()
        return


class E8257D(agilent):
    pass

class E8247C(agilent):
    machine_test = 'pass'


class sg83732(agilent):
    pass

class E8241A(agilent):
    pass

class N5183A(agilent):
    pass

