import os, sys, multiprocessing

dicoNotes = { "E1" : [10, 15, 20], "E2" : [12, 16, 15], "E3" : [11, 13, 20]}
N=len(dicoNotes)
listEtukey=dicoNotes.keys()
listEtu=[]
listMoy=[]
for i in listEtukey:
    listEtu.append(i)
dfr,dfw=multiprocessing.Pipe()
BestE=["Ex",0,0,0]


for i in range(N):
    PID_fils=os.fork()
    Etu=listEtu[i]
    if PID_fils!=0:
        listnote=dfr.recv()
        print(listnote) 
        listMoy.append(listnote[1]) 
    else:
        notes=dicoNotes[Etu]
        moy=0
        nbnote=len(notes)
        BestN=0
        WorstN=20
        for note in notes:
            moy+=note/nbnote
            if note>=BestN:
                BestN=note
            if note<=WorstN:
                WorstN=note
        dfw.send([Etu,moy,BestN,WorstN])
        sys.exit()

        
BestM=0
BestE=""
for Etu in range(N):
    if listMoy[Etu]>BestM:
        BestE=listEtu[Etu]
        BestM=listMoy[Etu]

print(BestM)
print(BestE)


