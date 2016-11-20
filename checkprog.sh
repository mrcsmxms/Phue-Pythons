#!/bin/sh
SERVICE1='/home/pi/Desktop/TasterR.py'
SERVICE2='/home/pi/Desktop/TasterA.py'
SERVICE3='/home/pi/Desktop/TasterL.py'


if ps ax | grep -v grep | grep $SERVICE1 > /dev/null
then
    echo "Taster R ist online"
else
    echo "Deamon Taster R ist abgestuerzt und wird neu gestartet"
    sudo python $SERVICE1 &
    echo "Taster R ist wieder online"
fi


if ps ax | grep -v grep | grep $SERVICE2 > /dev/null
then
    echo "Taster A ist online"
else
    echo "Deamon Taster A ist abgestuerzt und wird neu gestartet"
    sudo python $SERVICE2 &
    echo "Taster A ist wieder online"

fi

if ps ax | grep -v grep | grep $SERVICE3 > /dev/null
then
    echo "Taster L ist online"
else
    echo "Deamon Taster L ist abgestuerzt und wird neu gestartet"
    sudo python $SERVICE3 &
    echo "Taster L ist wieder online"
fi
