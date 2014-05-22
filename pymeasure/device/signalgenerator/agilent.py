#! /usr/bin/env python

import signalgenerator as sg

class agilent(sg.signalgenerator):
    api = {'freq_set': 'FREQ',
           'freq_check': 'FREQ?',
           'power_set': 'POW',
           'power_check': 'POW?',
           'output_on': 'OUTP 1',
           'output_off': 'OUTP 0',
           'output_check': 'OUTP?'}

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

