import os,sys
N = 10
i=1
while os.fork()==0 and i<=N :
    i += 1
print(i)
sys.exit(0)
# Il affiche tout les nombres de 0 à 11, chaque fonction fils va afficher un nombre et quand on sort de la boucle while on se trouve à 11 et cela l'affiche donc une deuxième fois