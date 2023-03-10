import os, signal,time,sys
global a
a=False
def Lance(s,frame):
    global a
    a=True
    return a
signal.signal(signal.SIGINT,Lance)

while a == False:
    time.sleep(2)
    print('Oui\n')
