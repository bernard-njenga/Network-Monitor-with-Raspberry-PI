#*/bin/bash

#set minimal threshold to go to the next step
minimal=0

#ping www.google.com with 10 retrials 
ping=$(ping -c 10 -W 1 www.google.com |grep -c 'ttl=*')

#if else statement to continue to next script if output is greater than 0 or less than 0
if [ $ping -gt $minimal ];
then
    echo "host reachable"
    python /home/pi/speedtest.py
else
    echo "host not reachable"
    python /home/pi/nospeedtest.py
fi

