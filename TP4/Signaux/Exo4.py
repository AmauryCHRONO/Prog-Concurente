import os, signal,time,sys
N=6
j=0
pid=os.fork()

if pid!=0:
    for i in range(N):
        time.sleep(1)
        print(i)
        if i == 3:
            os.kill(pid,signal.SIGKILL)


else:
    while True:
        time.sleep(1)
        print(str(j)+" fils")
        j+=1
        
            
