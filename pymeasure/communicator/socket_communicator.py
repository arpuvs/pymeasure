#! /usr/bin/env python

import socket
import communicator as com

class socket_communicator(com.communicator):
    method = 'socket'
    
    host = ''
    port = 9999
    timeout = 0
    family = ''
    type = ''
    
    def __init__(self, host, port, timeout=10,
                 family=socket.AF_INET,
                 type=socket.SOCK_STREAM,
                 open=True):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.family = family
        self.type = type
        if open: self.open()
        pass
    
    def open(self):
        #print('open', self.host, self.port) 
        self.sock = socket.socket(self.family, self.type)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))
        self.sockfp = self.sock.makefile()
        self.connection = True
        return

    def close(self):
        self.sock.close()
        self.connection = False
        return
        
    def send(self, msg):
        self.sock.send(msg)
        return
        
    def recv(self, byte=1024):
        ret = self.sock.recv(byte)
        return ret
    
    def readline(self):
        ret = self.sockfp.readline()
        return ret


class socket_dummy_communicator(socket_communicator):
    method = 'socket_dummy'
    
    def __init__(self, host, port, timeout=10,
                 family=socket.AF_INET,
                 type=socket.SOCK_STREAM):
        socket_communicator.__init__(self, host, port, timeout,
                                     family, type, open=False)
        pass
        
