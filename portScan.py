#!/usr/bin/env python3

import socket
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-hl", "--hostlist", required=True, help="Host List")
ap.add_argument("-p", "--port", required=True, help="What port to scan")
args = vars(ap.parse_args())

def scan_port(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    myPort = str(port)
    myHost = host.rstrip()
    screenText = myHost+':'+myPort
    logText = myHost+'\n'
    if result == 0:
        print(screenText+' Open')
        openResults.write(logText)
    else:
        print(screenText+' Closed')
        closedResults.write(logText)       
    sock.close()
    

if not os.path.isfile(args["hostlist"]):
    print('\n\nWe can\'t find/open %s.  Please check that it\'s a valid file.\n\n'%hostlist)
else:
    openResults = open(args['hostlist']+'.open.'+args["port"]+'.results.txt','w')
    closedResults = open(args['hostlist']+'.closed.'+args["port"]+'.results.txt','w')
    hosts = open(args["hostlist"], 'r')
    for line in hosts:
        scan_port(line,int(args["port"]))


openResults.close()
closedResults.close()