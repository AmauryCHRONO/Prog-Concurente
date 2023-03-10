import os

for i in range(3):
    pid=os.fork()
    p=os.getppid()
    f=os.getpid()
    print("("+str(i)+'), je suis le processus : '+str(f)+', mon pere est : '+str(p)+', retour : '+str(pid))