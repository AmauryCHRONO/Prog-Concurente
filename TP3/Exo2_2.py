import os, multiprocessing,sys
dfr1, dfw1 = multiprocessing.Pipe()
dfr2, dfw2 = multiprocessing.Pipe()
out=os.open("sortie.txt",os.O_WRONLY|os.O_CREAT,0o0644)

pid1=os.fork()

if pid1==0:
    dfw1.close()
    os.dup2(dfr1.fileno(),sys.stdin.fileno())
    dfr1.close()
    dfr2.close()
    os.dup2(dfw2.fileno(), 1)
    dfw2.close()
    os.execlp("grep","grep","chaine")

pid2=os.fork()

if pid2!=0:
    dfw2.close()
    dfr1.close()
    dfr2.close()
    os.dup2(dfw1.fileno(),sys.stdout.fileno())
    dfw1.close()
    os.execlp("sort","sort","fichier.txt") 

if pid2==0:  
    dfw2.close()
    dfr1.close()
    dfw1.close() 
    os.dup2(dfr2.fileno(),sys.stdin.fileno())
    dfr2.close()
    os.dup2(out, 1)
    os.execlp("tail","tail","-n","5")