import os, signal,time,sys,multiprocessing

def funP1(S,mutex):
    print('P1')
    time.sleep(5)
    mutex.acquire()
    S.value=True
    mutex.release()
    sys.exit(0)

def funP2(S,mutex):
    a=False
    while a==False:
        mutex.acquire()
        a=S.value
        mutex.release()

    print('P2')

    sys.exit(0)

mutex=multiprocessing.Lock()
S=multiprocessing.Value('i',False)

P1=multiprocessing.Process(target=funP1,args=(S,mutex))
P2=multiprocessing.Process(target=funP2,args=(S,mutex))
P1.start()
P2.start()
P1.join()
P2.join()