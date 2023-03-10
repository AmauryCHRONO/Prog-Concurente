import os, sys, multiprocessing
dfr,dfw=multiprocessing.Pipe()

if os.fork()!=0:
    dfr.close()  
    os.dup2(dfw.fileno(),1)
    dfw.close() 
    os.execlp("cat","cat","fichier.txt")

else:
    dfw.close()  
    os.dup2(dfr.fileno(),0)
    dfr.close() 
    os.execlp("wc","wc")