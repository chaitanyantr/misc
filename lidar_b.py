#!/usr/bin/env python

import sys
import smbus
import time

bus = smbus.SMBus(1)
LIDAR_ADR=0x62

def measure():

   bus.write_byte_data(LIDAR_ADR,0,4)
   bus.write_byte(LIDAR_ADR, 1)

   while bus.read_byte(LIDAR_ADR) & 1 != 0:
      pass
      
   bus.write_byte(LIDAR_ADR, 0xf)
   d=bus.read_byte(LIDAR_ADR)<<8
   bus.write_byte(LIDAR_ADR, 0x10)
   d |=bus.read_byte(LIDAR_ADR)
   
   return d

while(True):

   t0=time.time()
   
   d=measure()

   d_meters = d/100.0

   t1=time.time()
   
   print ("%3d %4d" % ((t1-t0)*1000,d))

