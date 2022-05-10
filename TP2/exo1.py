import os

print("Processus pere = %d" %(os.getpid()))

if os.fork():
    os.execlp("python","python","exo.py")

if os.fork():
    os.execlp("python","python","exoo.py")