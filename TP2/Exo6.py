import os, time, random, sys
for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(0,4)
time.sleep(delai)
try:
    os.wait()
except ChildProcessError:
    pass
print("Mon nom est " + chr(ord('A')+i) + " j ai dormi " +str(delai) + " secondes")
sys.exit(0)

# 1) C'est juste 5 programmes qui se cree a suit des uns les autres

# 2) Mon nom est D j ai dormi 2 secondes
#    Mon nom est A j ai dormi 3 secondes
#    Mon nom est D j ai dormi 3 secondes
#    Mon nom est B j ai dormi 4 secondes
#    Mon nom est C j ai dormi 4 secondes


