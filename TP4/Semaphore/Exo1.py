import os, signal,time,sys,multiprocessing

def funP1(L,S,mutex):
    i=1
    SI=0
    while(i<N):
        SI+=L[i]
        i+=2
    mutex.acquire()
    S.value+=SI
    mutex.release()
    sys.exit(0)

def funP2(L,S,mutex):
    i=0
    SP=0
    while(i<N):
        SP+=L[i]
        i+=2
    mutex.acquire()
    S.value+=SP
    mutex.release()
    sys.exit(0)

L=[1,2,3,4,5,6,7,8,9,10]
N=len(L)
mutex=multiprocessing.Lock()
S=multiprocessing.Value('i',0)

P1=multiprocessing.Process(target=funP1,args=(L,S,mutex))
P2=multiprocessing.Process(target=funP2,args=(L,S,mutex))
P1.start()
P2.start()
P1.join()
P2.join()

print(S.value)
print(sum(L))