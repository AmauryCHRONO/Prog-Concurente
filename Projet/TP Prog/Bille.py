import time,multiprocessing


def travail(bille):
    m=5
    while m>0:
        demandebille(bille)
        time.sleep(1*bille)
        retournebille(bille)
        m-=1
    mutex.acquire()
    Control.value+=1
    mutex.release()
    print("j'avais besoin de "+str(bille)+" billes j'ai finit")

def demandebille(bille):
    mutex.acquire()
    while nb_bille.value<bille:
        print('je suis en attente, je demande '+str(bille)+' billes')
        mutex.release()
        Sem.acquire()
        mutex.acquire()

    print("c'est bon j'ai "+str(bille)+" billes" )
    nb_bille.value-=bille
    mutex.release()
    Sem.release()
    

def retournebille(bille):
        mutex.acquire()
        nb_bille.value+=bille
        mutex.release()



def controleur():
    Test=0
    while Test<4:
        time.sleep(0.5)
        mutex.acquire()
        print("il y a "+str(nb_bille.value)+" billes")
        mutex.release()
        mutex.acquire()
        Test=Control.value
        mutex.release()
    print("Tout le monde a finit")

if __name__=='__main__':
    Sem=multiprocessing.Semaphore(0)
    mutex=multiprocessing.Lock()
    nb_bille=multiprocessing.Value('i',9)
    Control=multiprocessing.Value('i',0)

    C=multiprocessing.Process(target=controleur,args=())
    P1=multiprocessing.Process(target=travail,args=(5,))
    P2=multiprocessing.Process(target=travail,args=(3,))
    P3=multiprocessing.Process(target=travail,args=(4,))
    P4=multiprocessing.Process(target=travail,args=(2,))
    C.start()
    P1.start()
    P2.start()
    P3.start()
    P4.start()
    C.join()
    P1.join()
    P2.join()
    P3.join()
    P4.join()




