import os, signal,time,sys


def fun(s,frame):
    global okF
    if okF==False and s==signal.SIGUSR1 :
        okF=True
    else:
        sys.exit(0)



N=8
okF=False
stop=False
pid=os.fork()

if pid!=0:
    for i in range(N):
        time.sleep(1)
        print(i)
        if i == 3 or i==5:
            os.kill(pid,signal.SIGUSR1)
    os.kill(pid,signal.SIGUSR2)

else:
    j=0
    signal.signal(signal.SIGUSR1,fun)
    signal.signal(signal.SIGUSR2,fun)
    while True:
        time.sleep(1)
        if okF:
            print(str(j)+" fils")
            okF=False
        j+=1
        
        