#! /usr/bin/env python


class communicator(object):
    connection = False
    
    def __init__(self, *args):
        if len(args)!=0:
            self.open(*args)
            pass
        pass
    
    def open(self, *args):
        pass
    
    def close(self):
        pass
    
    def send(self, msg):
        pass
    
    def recv(self, byte):
        pass
        
    def readline(self):
        pass


