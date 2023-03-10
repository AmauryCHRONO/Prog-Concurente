import os

if os.fork() == 0:
    print('\nCommande Who :')
    os.execlp("who","who")
os.wait()
if os.fork() == 0:
    print('\nCommande ps :')
    os.execlp("ps","ps")
os.wait()
if os.fork() == 0:
    print('\nCommande ls -l :')
    os.execlp("ls","ls","-l")
os.wait()
print('\nFin du père')