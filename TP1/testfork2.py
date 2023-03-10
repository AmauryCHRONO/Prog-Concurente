import os,sys
for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("Ok !")
    print("Bonjour !")
sys.exit(0)

#30 Bonjour ! 15 OK ! 
#Boucle i=0:
#   -le père dit Ok et Bonjour et crée le fils P1
#   -le fils P1 dit Bonjours (car PID=0)
#    2 BJ et 1 OK
#Boucle i=1:
#   -le père dit Ok et Bonjour et crée le fils P2
#   -le fils P1 se comporte maintenant comme un père dit Bonjour et Ok et crée un fils P5
#   -le fils P5 et P2 dit Bonjours (car PID=0)
#   4 BJ et 2 OK
#Boucle i=2:
#   -le père dit Ok et Bonjour et crée le fils P3
#   -les fils P1,P5 et P2 se comportent comme des pères et disent Bonjour et Ok et créent un fils respectivement P6, P11 et P8
#   -les fils P3,P6, P11 et P8 disent Bonjour (car PID=0)
#   8 BJ et 4 OK
#Boucle i=3
#   -le père dis Ok et Bonjour et crée le fils P4,
#   -les fils P1,P5,P11,P6,P2,P8 et P3 se comportent comme des pères et disent Bonjour et Ok et créent un fils respectivement P15,P12,P13,P7,P14,P9 et P10
#   -les fils P15,P12,P13,P7,P14,P9,P10 et P4 disent Bonjour (car PID=0)
#   16 BJ et 8 OK