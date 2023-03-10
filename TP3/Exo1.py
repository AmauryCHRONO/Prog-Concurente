import os, sys, multiprocessing
dfr,dfw=multiprocessing.Pipe()
if os.fork()!=0:
    dfr.close()  
    dfw.send("Bonjour")    
    dfw.close() 


elif os.fork()!=0:
    dfw.close() 
    print(dfr.recv())
    dfr.close()    
