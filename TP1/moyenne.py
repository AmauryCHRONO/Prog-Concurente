import sys

moy=0
if len(sys.argv[1:])>=1:
    nbelement=len(sys.argv[1:])
    for note in sys.argv[1:]:
        try:
            note=float(note)
        except ValueError:
            print('Note non valide')
            sys.exit(1)
        if note<=20 and note>=0:
            moy+=note/nbelement
        elif note>20 or note<0:
            print('Note non valide')
            sys.exit(2)


    print("Moyene = "+"%.2f"%moy)

else:
    print('Note non valide')
