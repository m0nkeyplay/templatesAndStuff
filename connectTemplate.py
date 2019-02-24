#!/usr/bin/python3
#
#  Simple Connection Template
#  Usually need these imports so leaving them in


from sys import argv
import time
import socket
import string
import re


SERVER = ''
PORT =


sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_conn():
    sconn.connect((SERVER, PORT))
    print("Connected to %s %s" % (SERVER, PORT))

def send_data(command):
    sconn.send(bytes(command + '\n', 'utf-8'))

#   Connect
server_conn()


#   Do Something with the data
while (1):
    text=sconn.recv(2040)
    text= str(text)
