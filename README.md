# Network-Monitor-with-Raspberry-PI
Track how your internet Service provider is performing on their speeds and get email updates of the historical data. 

The project involves having a router and a raspberry device. The solution here involves the Raspberry PI doing speedtests after every 15minutes to check on the service being offered. The setup sends the logs to a csv file save locally. At the beginning of the next day, another query executes to send an email to your account sowing the stats picked so far.

Happy Testing this solution. :-)  

Start by updating the Raspberry PI
#Sudo apt-get update
#sudo apt-get upgrade

Install the Speedtest App
#sudo apt-get speedtest-cli

Create the Bash script to execute the python file speedtest
#sudo nano speedtest.sh

Create the Python file to execute the speedtest app
#Sudo nano speedtest.py

Create the Bash script to execute the pyhton file sendemail
#sudo nano sendemail.sh

Create the Python file to execute the sendemail function
#sudo nano sendemail.py

Create Cron jobs for the tasks. First task of taking the speed counters runs after every 15mins and the second task of sending email runs everyday at 8am
#*/15 * * * * /home/pi/speedtest.sh
#0 8 * * * /home/pi/sendemail.sh
