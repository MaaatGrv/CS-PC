import os,sys

N=10

for i in range(N):
    pid = os.fork()
    if pid == 0 :
        print("Je suis", os.getpid(), "mon père est", os.getppid())
        break
sys.exit(0)