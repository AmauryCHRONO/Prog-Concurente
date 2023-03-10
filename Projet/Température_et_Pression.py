#---------------------------------------------------------
# Créateur : CHRONOWSKI Amaury / JOBERT--ROLLIN Gabin
# Crée le : 10/06/2022
# Programme : Control de la température et de la pression via un système multiprocessing
#---------------------------------------------------------

# Bibliothèques
import time,multiprocessing,random

# Programme secondaires

# Programme du controleur, met en route/arrête le chauffage et la pompe en fonction de la température et de la pression et arrete tout les processus au bout d'un certain temps en fonction de boucle (le nombre de boucle que fait le programme de controle)
def Control(T_ref,P_ref): #Entrées = T_ref : la température voulue / P_ref : la pression voulue

    boucle=250

    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.2)
        mutex.acquire()

        if T.value>T_ref: 
            go_chauffage.value=False
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value=False


        elif T.value<T_ref: 
            go_chauffage.value=True
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value=False


        elif T.value==T_ref: 
            go_chauffage.value=False
            if P.value>P_ref: 
                go_pompe.value=True
            else: 
                go_pompe.value==False


        if boucle==0:
            on.value=False
        else:
            boucle-=1
    mutex.release()



# Programme du chauffage, augmente la température quand elle est trop faible
def Chauffer():

    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.1)
        mutex.acquire()
        if go_chauffage.value:
            T.value+=0.5
    mutex.release()



# Programme de la pompe, diminue la pression quand elle est trop faible
def Pomper():

    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.1)
        mutex.acquire()
        if go_pompe.value:
            P.value-=2
    mutex.release()



# Programme qui relève la temprérature, en réalité il simule une diminution aléatoire de température que l'on pourrait relever
def Temp():

    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.5)
        mutex.acquire()
        T.value-=0.5*random.random()
    mutex.release()



# Programme qui relève la pression, en réalité il simule une augmentation aléatoire de pression que l'on pourrait relever
def Pres():
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(0.5)
        mutex.acquire()
        P.value+=2*random.random()
    mutex.release()

# Programme qui réstitue les données à l'utilisateur, il affiche la température et la pression pour un instant T
def Screen():
    mutex.acquire()
    while on.value:
        mutex.release()
        time.sleep(1)
        mutex.acquire()
        print("La température est de "+str(T.value)+" °C")
        print("La pression est de "+str(P.value)+" pa")



# Programme principale
if __name__=='__main__':

    # Initialisation du verrou
    mutex=multiprocessing.Lock()

    # Initialisation des variable partagées
    go_pompe=multiprocessing.Value('i',False) # Variable qui met en route/arrête la pompe (True/False)
    go_chauffage=multiprocessing.Value('i',False) # Variable qui met en route/arrête le chauffage (True/False)
    T=multiprocessing.Value('f',25) # Variable qui stocke la dernière température relevée (Float)
    P=multiprocessing.Value('f',1013) # Variable qui stocke la dernière pression relevée (Float)
    on=multiprocessing.Value('i',True) # Variable qui indique si les processus s'arrêtent en fonction du controleur (True/False)

    # Saisie de la température et pression voulues
    T_ref=int(input("Veuiller rentrer la température voulue :\n"))
    P_ref=int(input("Veuiller rentrer la pression voulue :\n"))

    # Initialisation des processus
    Controleur=multiprocessing.Process(target=Control,args=(T_ref,P_ref,)) # Process pour le controleur qui gère la température et pression (Entrée = T_ref : Température voulue, P_ref : Pression voulue)
    Chauffage=multiprocessing.Process(target=Chauffer,args=()) # Process pour le chauffage
    Pompe=multiprocessing.Process(target=Pomper,args=()) # Process Pour la pompe
    Température=multiprocessing.Process(target=Temp,args=()) # Process qui récupère la température
    Pression=multiprocessing.Process(target=Pres,args=()) # Process  qui récupère la pression
    Ecran=multiprocessing.Process(target=Screen,args=()) # Process qui affiche la température et la pression à un instant T

    # Lancement des processus
    Controleur.start()
    Chauffage.start()
    Pompe.start()
    Température.start()
    Pression.start()
    Ecran.start()

    Controleur.join()
    Chauffage.join()
    Pompe.join()
    Température.join()
    Pression.join()
    Ecran.join()
