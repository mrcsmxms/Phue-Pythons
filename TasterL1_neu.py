#!/usr/bin/python2

import datetime
now = datetime.datetime.now()
import sys; sys.path.append("/home/pi/phue-master")
import RPi.GPIO as GPIO
import time
import urllib2
from xml.dom import minidom

from phue import Bridge

InPin = 23 #GPIO-PIN des Tasters (BCM)
IP = '192.168.178.69' # IP-Adresse der Bridge
DimTimeON = 0 # Dimmzeit beim Einschalten in sek
DimTimeOFF = 0 # Dimmzeit beim Ausschalten in sek
Brightness1 = 33 # Helligkeit in %
Brightness2 = 66
Brightness3 = 100

DimTimeOn = DimTimeON*10 # in 1/10 sek
DimTimeOff = DimTimeOFF*10 # in 1/10 sek
bri1 = Brightness1*1000/100*254/1000
bri2 = Brightness2*1000/100*254/1000
bri3 = Brightness3*1000/100*254/1000
commandOn1 =  {'transitiontime' : DimTimeOn, 'on' : True, 'bri' : bri1}
commandOn2 =  {'transitiontime' : DimTimeOn, 'on' : True, 'bri' : bri2}
commandOn3 =  {'transitiontime' : DimTimeOn, 'on' : True, 'bri' : bri3}
commandOff = {'transitiontime' : DimTimeOff, 'on' : False}

b = Bridge(IP)                                         

GPIO.setmode(GPIO.BCM)

GPIO.setup(InPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(InPin)
    if input_state == False:
        print
        print now.strftime("%Y-%m-%d %H:%M")
        print('linker Knopf gedrueckt')
        if b.get_light(2,'bri') <= 0 or b.get_light(2,'on') == False :                                     
            b.set_light(2, commandOn1)
            print "Stufe 1"
            #print "linkes Licht aus in %d Sekunden" % DimTimeOFF

        elif b.get_light(2,'bri') > 0 and b.get_light(2,'bri') <= bri1:                               
            b.set_light(2, commandOn2)
            print "Stufe 2"
            
            #print "linkes Licht an auf %d Prozent in %d Sekunden" % (Brightness, DimTimeON)
        elif b.get_light(2,'bri') > bri1 and b.get_light(2,'bri') <= bri3-1:
            b.set_light(2, commandOn3)
            print "Stufe 3"
        else:
            b.set_light(2, commandOff)
            print "Aus"
        time.sleep(0.2)
