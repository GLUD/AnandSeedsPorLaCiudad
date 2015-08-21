#!/usr/bin/python
import urllib2
import serial
import time
import commands

url = 'http://10.40.21.174/acciones.txt'
response = urllib2.urlopen(url)
html = response.read()

print 'Obteniendo datos de: ' + url
print 'Parametros: ' + html

dev = commands.getoutput("ls /dev/ttyACM*")
print 'Arduino is in device: ' + dev
ser = serial.Serial(dev, 9600 )

try:
    while True:
	response = urllib2.urlopen(url)
	html = response.read()
        #ser.write('hums=1000&huma=10000&tems=50.3&tema=20.2')
	ser.write(html)
	time.sleep(1)
	bytesToRead = ser.inWaiting()
	response = ser.read(bytesToRead)
	#response = ser.readline()
        if len(response)>0:
            print response
except KeyboardInterrupt:
    ser.close()

