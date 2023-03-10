import os,sys

N=int(sys.argv[1])

for i in range(2,N):
    pid = os.fork()
    if pid>0:
        print("pere",os.getpid())
    else:
        print("fils",os.getpid())
        sys.exit(0)

#Le père crée un fils, le fils sort du programme (ligne 11), le pere continue à créer des fils qui sortent du programme donc il est bien le seul père du programme