#! /usr/bin/env python

import signalgenerator as sg

class agilent(sg.signalgenerator):
    api = {'freq_set': 'FREQ¥n',
           'freq_check': 'FREQ?\n',
           'power_set': 'POW\n',
           'power_check': 'POW?\n',
           'output_on': 'OUTP 1\n',
           'output_off': 'OUTP 0\n',
           'output_check': 'OUTP?\n'}

class E8257D(agilent):
    pass

class E8247C(agilent):
    pass

class sg83732(agilent):
    pass

class E8241A(agilent):
    pass

class N5183A(agilent):
    pass

