import os, signal,time,sys

def rien(s,frame):
    print('GOT HIM')

signal.signal(signal.SIGINT,rien)
while True:
    time.sleep(5)
    print('Oui')
