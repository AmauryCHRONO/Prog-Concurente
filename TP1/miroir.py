import sys

miroir=""
if len(sys.argv)>1:
    for lettre in sys.argv[1]:
        miroir=lettre+miroir
print(miroir)
    
