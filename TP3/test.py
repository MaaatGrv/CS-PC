import multiprocessing as mp
import sys

def Processp1 (sem1,sem2,N,L,somme):
    i=1
    SommeImpaire=0
    while i<N:
        SommeImpaire += L[i]
        i+=2
    sem1.acquire()    
    somme.value +=SommeImpaire
    
    sem1.release()
    sys.exit(0)

def Processp2 (sem1,sem2,N,L,somme):
    
    i=0
    SommePaire=0
    while i<N:
        SommePaire += L[i]
        i+=2
    
    sem1.acquire()
    
    somme.value+=SommePaire
    
    sem1.release()
    sys.exit(0)

somme =mp.Value('i',0)
L=[1,2,3,4,5,6,7,8,9,10]
N=len (L)

sem1=mp.Semaphore(1)
sem2=mp.Semaphore(1)
p1 = mp.Process(target = Processp1 , args = (sem1,sem2,N,L,somme))
p2 = mp.Process(target = Processp2 , args = (sem1,sem2,N,L,somme))
p1.start()
p2.start()

p1.join()
p2.join()
print ((somme.value))
