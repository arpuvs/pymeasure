#! /usr/bin/env python

import random
import pymeasure


def port_generate(index):
    base_port = 50000
    return base_port + random.randrange(index*1000, (index+1)*1000)
    

"""
# signalgenerator
# ===============
com_sg = pymeasure.socket_communicator('127.0.0.1', port_generate(0))
sg = pymeasure.signalgenerator.dummy(com_sg)
sg.self_test(0.05)
sg.server_stop()

# powermeter
# ==========
com_pm = pymeasure.socket_communicator('127.0.0.1', port_generate(1))
pm = pymeasure.powermeter.dummy(com_pm)
pm.self_test(0.05)
pm.server_stop()

# spectrumanalyzer
# ==========
com_sa = pymeasure.socket_communicator('127.0.0.1', port_generate(2))
sa = pymeasure.spectrumanalyzer.dummy(com_sa)
sa.self_test(0.05)
sa.server_stop()
"""


# daq
# ===
com_daq = pymeasure.socket_communicator('127.0.0.1', port_generate(0))
daq = pymeasure.daq.dummy(com_daq)
daq.self_test(0.05)
daq.server_stop()


