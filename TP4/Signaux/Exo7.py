import os, signal,time,sys
Time=5
print("Entrer un entier en moins de "+str(Time)+" s\n")
pid=os.fork()

if pid!=0:
    for i in range(Time):
        time.sleep(1)
    os.kill(pid,signal.SIGKILL)
    print("Trop tard")
    sys.exit(0)

else:
    while True:
        try:
            Entrer=int(input('svp un entier : '))
            print("ok merci")
            os.kill(pid,signal.SIGKILL)
        except:
            pass