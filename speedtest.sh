#*/bin/bash

minimal=0
#ping=$(ping -c 1 -W 1 www.google.com |egrep -F 'ttl=') 
ping=$(ping -c 10 -W 1 www.google.com |grep -c 'ttl=*')

if [ $ping -gt $minimal ];
then
    echo "host reachable"
    python /home/pi/speedtest.py
else
    echo "host not reachable"
    python /home/pi/nospeedtest.py
fi

