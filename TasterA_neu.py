#!/usr/bin/python2

import datetime
import sys; sys.path.append("/home/pi/phue-master")
import RPi.GPIO as GPIO
import time
import urllib2
from xml.dom import minidom
from phue import Bridge

InPin = 18 #GPIO-PIN des Tasters (BCM)
IP = '192.168.178.69' # IP-Adresse der Bridge
DimTimeON = 3 # Dimmzeit beim Einschalten in sek
DimTimeOFF = 6 # Dimmzeit beim Ausschalten in sek
Brightness = 100 # Helligkeit in %


DimTimeOn = DimTimeON*10 # in 1/10 sek
DimTimeOff = DimTimeOFF*10 # in 1/10 sek
bri = Brightness*1000/100*254/1000
commandOn =  {'transitiontime' : DimTimeOn, 'on' : True, 'bri' : bri}
commandOff = {'transitiontime' : DimTimeOff, 'on' : False}

b = Bridge(IP)
GPIO.setmode(GPIO.BCM)
GPIO.setup(InPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    now = datetime.datetime.now() 
    input_state = GPIO.input(InPin)
    if input_state == False:
        if b.get_light(1,'on') == True:
         Status1 = "An"
        else:
         Status1 = "Aus"
       
        if b.get_light(2,'on') == True:
         Status2 = "An"
        else:
         Status2 = "Aus"
        print "------------------------"
        print
        print now.strftime("%d.%m.%Y %H:%M:%S")
        print "Mittlerer Knopf gedrueckt"
        print
        print "LINKS"
        print "Status: %s" % Status2
        print "Aktuelle Helligkeit: %d Prozent, %d Lumen" % ((b.get_light(2,'bri'))*1000/254*100/1000,  (b.get_light(2,'bri'))*1000/254*806/1000)
        print
        print "RECHTS"
        print "Status: %s" % Status1
        print "Aktuelle Helligkeit: %d Prozent, %d Lumen" % ((b.get_light(1,'bri'))*1000/254*100/1000,  (b.get_light(1,'bri'))*1000/254*806/1000) 
        if b.get_light(2,'on') == True:                                    
            b.set_light( [1,2], commandOff)
            print
            print "beide Lichter aus in %d Sekunden" % DimTimeOFF
        else:                               
            b.set_light( [1,2],commandOn)
            print
            print "beide Lichter an auf %d Prozent in %d Sekunden" % (Brightness, DimTimeON)
        time.sleep(0.2)












