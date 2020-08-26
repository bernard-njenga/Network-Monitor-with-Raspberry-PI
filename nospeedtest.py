import os
import re
import time

try:
    f = open('/home/pi/speedtest/speedtestrpi_1.csv', 'a+')
    if os.stat('/home/pi/speedtest/speedtestrpi_1.csv').st_size == 0:
            f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
except:
    pass

f.write('{},{},{},{},{}\r\n'.format(time.strftime('%d/%m/%y'), time.strftime('%H:%M'),'0','0','0'))

