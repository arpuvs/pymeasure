#! /usr/bin/env python

import pymeasure


# signalgenerator
# ===============
com_sg = pymeasure.socket_dummy_communicator('localhost', 55001)
sg = pymeasure.signalgenerator.dummy(com_sg)
sg.self_test()
sg.server_stop()



