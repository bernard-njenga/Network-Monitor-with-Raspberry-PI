#*/bin/bash

while ! ping -c 1 -W 1 www.google.com; do
    echo "Waiting for www.google.com - network interface might be down..."
    sleep 10
done
python /home/pi/sendemail2.py
echo "email sent"
#while ! ip route | grep -oP default via .+ dev eth0; do
 # echo interface not up, will try again in 1 second;
 # sleep 1;
#done
#echo interface up

#until  cat /sys/class/net/eth0/operstate -eq up
#      echo connected
#      sleep 1
#done
#python /home/pi/sendemail2.py
# echo do script
 

