# 17.05.22
# @Mathis Gorvien

import sys
import multiprocessing as mp

liste=[1,68,5,5,26,5,98,4,5,1,47,2,3,14,8,99,2]
n=len(liste)

sem = mp.Semaphore(1)
mutex = mp.Lock()
Somme = mp.Value('i', 0)

#Processus P1
def fP1(pliste):
    SommeImpairs=0
    for i in range(n-1):
        SommeImpairs+=pliste[2*n+1]

    sem.acquire()
    mutex.acquire()

    Somme+=SommeImpairs

    mutex.release()
    sem.release()
    sys.exit(0)

#Processus P2
def fP2(pliste):
    SommePairs=0
    for i in range(n-1):
        SommePairs+=pliste[2*n]
    
    sem.acquire()
    mutex.acquire()

    Somme+=SommePairs

    mutex.release()
    sem.release()
    sys.exit(0)

P1 = mp.Process(target = fP1, args = (liste,))
P2 = mp.Process(target = fP2, args = (liste,))

P1.start()
P2.start()

P1.join()
P2.join()

print(Somme.value)
print("Verif :", sum(liste))

sys.exit(0)