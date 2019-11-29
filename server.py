# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("", 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096).decode()
        if not data: break
        from_client += data
        print (from_client)
        send_str='I am SERVER\n'
        send_str_enc = send_str.encode()
        conn.send(send_str_enc)
    conn.close()
    print ('client disconnected')