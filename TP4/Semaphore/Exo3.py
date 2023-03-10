import sys,multiprocessing,random

def funP1(N):
    for i in range(N):
        Q1.put(random.randint(0,10))
    sys.exit(0)

def funP2(N):
    for i in range(N):
        Q2.put(random.randint(0,10))
    sys.exit(0)



def funC1(N):
    for i in range(N):
        Sem1.acquire()
        a=Q1.get()
        Sem2.release()
        print("P1 "+str(a))

def funC2(N):
    for i in range(N):
        Sem2.acquire()
        a=Q2.get()
        Sem1.release()
        print("P2 "+str(a))


N=5
Q1=multiprocessing.Queue()
Q2=multiprocessing.Queue()
Sem1=multiprocessing.Semaphore(1)
Sem2=multiprocessing.Semaphore(0)
P1=multiprocessing.Process(target=funP1,args=(N,))
P2=multiprocessing.Process(target=funP2,args=(N,))
C1=multiprocessing.Process(target=funC1,args=(N,))
C2=multiprocessing.Process(target=funC2,args=(N,))
P1.start()
P2.start()
C1.start()
C2.start()
P1.join()
P2.join()
C1.join()
C2.join()