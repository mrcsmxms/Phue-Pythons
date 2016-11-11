import datetime
import sys; sys.path.append("/home/pi/phue-master")
import RPi.GPIO as GPIO
import time
import urllib2
from xml.dom import minidom
from phue import Bridge

InPin = 23 #GPIO-PIN des Tasters (BCM)
IP = '192.168.178.69' # IP-Adresse der Bridge
DimTimeON = 2 # Dimmzeit beim Einschalten in sek
DimTimeOFF = 3 # Dimmzeit beim Ausschalten in sek
Brightness = 50 # Helligkeit in %

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
        if b.get_light(2,'on') == True:
         StatusL = "An"
        else:
         StatusL = "Aus"
        print "------------------------"
        print
        print now.strftime("%d.%m.%Y %H:%M:%S")
        print "Linker Taster gedrueckt"
        print "Status : %s" % StatusL 
        print "Aktuelle Helligkeit: %d Prozent, %d Lumen" % ((b.get_light(2,'bri'))*1000/254*100/1000,  (b.get_light(2,'bri'))*1000/254*806/1000)
        if b.get_light(2,'on') == True:
            b.set_light(2, commandOff)
            print
            print "linkes Licht aus in %d Sekunden" % DimTimeOFF

        elif b.get_light(2,'on') == False or b.get_light(2,'bri') < 1:                               
            b.set_light(2, commandOn)
            print
            print "linkes Licht auf %d Prozent in %d Sekunden" % (Brightness, DimTimeON)
        time.sleep(0.2)
