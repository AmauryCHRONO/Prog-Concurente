import random,multiprocessing, time

#Calcul Multi−Processus 
def frequence_de_hits_pour_n_essais_multi(nb_iteration):
    count=0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1:
            count+=1 
    mutex.acquire()
    nb_hits_multi.value+=count
    mutex.release()

#Calcul Mono−Processus 
# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
def frequence_de_hits_pour_n_essais(nb_iteration):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1: count += 1
    return count

if __name__=='__main__':
    
    #Nombre d'hitération
    N=1000000
    print("\nOn fait "+str(N)+" itérations")
    #Nombre de Processus
    nb_proce=4
    
    #Multi-Processus
    #Création de la variable partagé
    debut_multi=time.time()
    mutex=multiprocessing.Lock()
    nb_hits_multi=multiprocessing.Value('i',0)

    #Création et lancemant des N Ptocessus
    with multiprocessing.Pool(nb_proce) as p:
        p.map(frequence_de_hits_pour_n_essais_multi,[int(N/nb_proce)]*nb_proce)
    fin_multi=time.time()

    #Calcule du temps de processe
    temps_multi=fin_multi-debut_multi

    #Affichage des résultats
    print("\nPour "+str(nb_proce)+" processus")
    print("Valeur estimée Pi par la méthode Multi−Processus : ",  4*nb_hits_multi.value / N)
    print("Le temps du multi-processus est",temps_multi)



    #Mono-Processus
    debut_mono=time.time()
    nb_hits_mono=frequence_de_hits_pour_n_essais(N)
    fin_mono=time.time()

    #Calcule du temps de processe
    temps_mono=fin_mono-debut_mono

    #Affichage des résultats
    print("\nPour le mono-processus")
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits_mono / N)
    print("Le temps du mono-processus est",temps_mono)



