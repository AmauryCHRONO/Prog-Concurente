import os,sys,time

N=int(sys.argv[1])


for i in range(1,N):
    pid_fils=os.fork()
    if pid_fils==0:
        print('Son PID : '+str(os.getpid()))
        print('Le PID de son pere : '+str(os.getppid()))
        time.sleep(2*i)
        print("Le fils a fini d'attendre")
        sys.exit(i)
    else:
        pid_fils,etat=os.wait()
        print('Leur identité : '+ str(pid_fils))
        print('Leur etat : '+str(etat))
