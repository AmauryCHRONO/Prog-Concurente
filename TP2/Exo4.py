import os,sys
n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2
        os.wait() #3
        n = i*2
        break
print("n = ", n) #4
sys.exit(0)


# 1) On se trouve dans le père car le PID est different de 0. Le PID est nul pour le fils.

# 2) Oui, on obtient toujours les même valeur donc ce programme reste constant et est donc détreministe

# 3) Il continue d'afficher la même chose mais il n'est pas focement détrministe car tout les processuce s'execute au même moment donc on est pas sur de se qu'il va s'afficher en premier

# 4) n = 0
#    n = 8
#    n = 6
#    n = 4
#    n = 2

# 5) Non
