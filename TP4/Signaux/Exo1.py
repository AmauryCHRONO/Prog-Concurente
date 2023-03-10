import os, signal,time,sys

def stop(s,frame):
    print("Signal reçu")
    sys.exit()

signal.signal(signal.SIGINT,stop)
while True:
    time.sleep(5)
    print('Oui')

