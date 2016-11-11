echo "all switch-daemons are going down"
#kill all switch-daemon
sudo pkill -f /home/pi/Desktop/TasterR_neu.py
sudo pkill -f /home/pi/Desktop/TasterL_neu.py
sudo pkill -f /home/pi/Desktop/TasterA_neu.py
echo "And they are back up"
#restart all switch-daemon
sudo python /home/pi/Desktop/TasterR_neu.py &
sudo python /home/pi/Desktop/TasterL_neu.py &
sudo python /home/pi/Desktop/TasterA_neu.py &
echo "!"
