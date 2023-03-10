import os, signal,time,sys
def rien(s,frame):
    print('GOT HIM')

N=6
j=0
pid=os.fork()

if pid!=0:
    for i in range(N):
        time.sleep(1)
        print(i)


else:
    signal.signal(signal.SIGINT,rien)
    while True:
        time.sleep(1)
        print(str(j)+" fils")
        j+=1

# C'EST QUELE PERE QUI RECOIT