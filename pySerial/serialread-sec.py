#!/usr/bin/python
import serial
import time
import commands
dev = commands.getoutput("ls /dev/ttyACM*")
print 'Arduino is in device: ' + dev
ser = serial.Serial(dev, 9600 )

try:
    while True:
        #ser.write('hums=1000&huma=10000&tems=50.3&tema=20.2')
	ser.write('valv=off')
	time.sleep(1)
	bytesToRead = ser.inWaiting()
	response = ser.read(bytesToRead)
	#response = ser.readline()
        if len(response)>0:
            print response
except KeyboardInterrupt:
    ser.close()

