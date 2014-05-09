#! /usr/bin/env python

import communicator as com

class dummy_communicator(com.communicator):
    def open(self, *args):
        print('open', args)
        self.connection = True
        return True

    def close(self):
        print('close')
        self.connection = False
        return True
        
    def send(self, msg='test_message\n'):
        if not self.connection: return False
        print('send', msg)
        return True
        
    def recv(self, byte=10):
        if not self.connection: return ''
        print('recv', byte)
        return 'test_message\n'[:byte]
    
    def readline(self):
        if not self.connection: return ''
        print('readline')
        return 'test_message\n'

