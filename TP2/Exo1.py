import os

pid=os.fork()
if pid>0:
    print('pere')
    os.execlp('python', 'python', 'test1.py')
    
else:
    print('fils')
    os.execlp('python', 'python', 'test2.py')