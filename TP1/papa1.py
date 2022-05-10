import os,sys

N=10
i=2

while os.fork()==0 and i <N:
    i+=1
    print("Je suis", os.getpid(), "mon père est", os.getppid())
sys.exit(0)