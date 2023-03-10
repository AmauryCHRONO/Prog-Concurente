import os,sys

N=int(sys.argv[1])

for i in range(2,N):
    pid = os.fork()
    if pid>0:
        print("pere",os.getpid())
        sys.exit(0)
    else:
        print("fils",os.getpid())

#Le père crée un fils et sort du programme (ligne 9) le fils dans la boucle suivante va faire la même chose donc on a bien le fils n qui crée le fils n+1