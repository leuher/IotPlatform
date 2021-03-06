#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'主模块'
__author__ = 'kakake'

import sys
from heartbeathandle import heartbeathandle
from gpiohandle import gpiohandle
#import test1


def main():
    try:
        threads={}

        if len(sys.argv)  == 2:
	        #print len(sys.argv)
	        heartbeat=heartbeathandle('heartbeat',2,sys.argv[1])
	        threads['heartbeat']=heartbeat
	
	        gpio=gpiohandle('gpio',1,sys.argv[1])
	        threads['gpio']=gpio
        else:
	        heartbeat=heartbeathandle('heartbeat',2)
	        threads['heartbeat']=heartbeat
	
	        gpio=gpiohandle('gpio',1)
	        threads['gpio']=gpio

          #启动线程
        for (name, value) in threads.items():
	        value.setDaemon(True)#守护线程
	        value.start()
        print "Started!!!"

        for (name, value) in threads.items():
            value.join()
        print "Stopped!!!"
    except Exception,ex:
        print "Stopped!!!",Exception,":",ex

if __name__ == '__main__':
    main()
