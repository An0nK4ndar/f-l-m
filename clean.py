import re , sys , os
from platform import system
from time import sleep
from threading import Thread
import time

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

dict={'mail.': '', 'cpanel.': '', 'cpcontacts.': '', 'webmail.':'', 'ftp.':'', 'autodiscover.':'', 'cpcalendars.':'', 'webdisk.':'', 'www.':''}
fout = open("input1877.txt", "wt")

with open("oxy.txt") as fp:
    line = fp.readline()
    while line:
        for k, v in dict.items():
            line = line.replace(k, v)

        print(line)
        fout.write(line)
        line = fp.readline()
fout.close()

print("Telegram : @Overthinker1877\n")
c = open("input1877.txt" , 'r').readlines()
c_set = set(c)
dz = open("input1877.txt" , 'w')
for line in c_set:
    dz.write(line)
prefix = 'http://'
suffix = '/'

with open('input1877.txt', 'r') as src:
    with open('output1877.txt', 'w') as dest:
       for line in src:
           dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))

