import os, sys, multiprocessing,random

dfr1,dfw1=multiprocessing.Pipe()
dfr2,dfw2=multiprocessing.Pipe()
dfr3,dfw3=multiprocessing.Pipe()
dfr4,dfw4=multiprocessing.Pipe()
sP=0
sI=0
stopP=0
stopI=0
if os.fork()!=0:   
    for i in range(int(sys.argv[1])):
        nb=random.randint(0,100)
        if  nb%2==0:
            dfw1.send(nb)
        else:
            dfw2.send(nb)
    dfw1.send(-1)
    dfw2.send(-1) 
    print("Somme des nombres pair : "+str(dfr3.recv()))
    print("Somme des nombres impair : "+str(dfr4.recv()))

else:
    if os.fork()!=0:
        while stopP!=-1:
            NbP=dfr1.recv()
            if NbP==-1:
                stopP=-1
            else:
                sP+=NbP
        dfw3.send(sP)

    else:
        while stopI!=-1:
            NbI=dfr2.recv()
            if NbI==-1:
                stopI=-1
            else:
                sI+=NbI
        dfw4.send(sI)