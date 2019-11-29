# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:13:56 2019

@author: Sergey Babenkov
"""

#!/usr/bin/env python3

import socket
import time
def sr(send_str):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('172.25.10.110',8080))
    send_str_enc=send_str.encode()
    client.send(send_str_enc)
    from_server=client.recv(4096)
    from_server_dec=from_server.decode()
    client.close()
    return from_server_dec

while True:
    ret_str=sr("True")
    print (ret_str)
    time.sleep(2)
    ret_str=sr("False")
    print (ret_str)
    time.sleep(2)
    
