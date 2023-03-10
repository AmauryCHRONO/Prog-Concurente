import multiprocessing,sys,os

from TP4.Semaphore.Exo4 import P3, funP3
def funR1():
    print("oui")
    
def funR2():
    print("oui")

def funR3():
    print("oui")

def funR4():
    print("oui")

def funE1():
    print("oui")

def funE2():
    print("oui")


Sem1=multiprocessing.Semaphore(0)
Sem2=multiprocessing.Semaphore(0)
Sem3=multiprocessing.Semaphore(0)
Sem4=multiprocessing.Semaphore(0)
Sem5=multiprocessing.Semaphore(0)
Sem6=multiprocessing.Semaphore(0)

R1=multiprocessing.Process(target=funR1,args=())
R2=multiprocessing.Process(target=funR2,args=())
R3=multiprocessing.Process(target=funR3,args=())
R4=multiprocessing.Process(target=funR4,args=())
E1=multiprocessing.Process(target=funE1,args=())
E2=multiprocessing.Process(target=funE2,args=())
R1.start()
R2.start()
R3.start()
R4.start()
E1.start()
E2.start()
R1.join()
R2.join()
R3.join()
R4.join()
E1.join()
E2.join()