#! /usr/bin/env python

import signalgenerator as sg

class agilent(sg.signalgenerator):
    api = {'freq_set': '',
           'freq_check': '',
           'power_set': '',
           'power_check': '',
           'output_on': '',
           'output_off': '',
           'output_check': ''}

class E8257D(agilent):
    pass

class E8247C(agilent):
    pass

class sg83732(agilent):
    pass

