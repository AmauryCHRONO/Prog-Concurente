import os

if os.fork() == 0:
    os.execlp("who","who")
if os.fork() == 0:
    os.execlp("ps","ps")
if os.fork() == 0:
    os.execlp("ls","ls","-l")