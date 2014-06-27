#! /usr/bin/env python

import random
import pymeasure

base_port = 55000


# signalgenerator
# ===============
com_sg = pymeasure.socket_dummy_communicator('127.0.0.1', base_port+random.randrange(-5000, -4000))
sg = pymeasure.signalgenerator.dummy(com_sg)
sg.self_test(0.05)
sg.server_stop()

# powermeter
# ==========
com_pm = pymeasure.socket_dummy_communicator('127.0.0.1', base_port+random.randrange(-4000, -3000))
pm = pymeasure.powermeter.dummy(com_pm)
pm.self_test(0.05)
pm.server_stop()



