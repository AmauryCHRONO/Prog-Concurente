import multiprocessing


def funP3():
    Sem2.release()
    Sem1.release()
    Sem3.acquire()
    Sem3.acquire()
    print("P3")

def funP1():
    Sem2.release()
    Sem3.release()
    Sem1.acquire()
    Sem1.acquire()
    print("P1")

def funP2():
    Sem3.release()
    Sem1.release()
    Sem2.acquire()
    Sem2.acquire()
    print("P2")

Sem1=multiprocessing.Semaphore(0)
Sem2=multiprocessing.Semaphore(0)
Sem3=multiprocessing.Semaphore(0)
P1=multiprocessing.Process(target=funP1,args=())
P2=multiprocessing.Process(target=funP2,args=())
P3=multiprocessing.Process(target=funP3,args=())

P1.start()
P2.start()
P3.start()
P1.join()
P2.join()
P3.join()
