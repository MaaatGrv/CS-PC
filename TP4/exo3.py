import sys
import random as rd
import multiprocessing as mp


N = 5

semQ1 = mp.Semaphore(1)
semQ2 = mp.Semaphore(1)
semC1 = mp.Semaphore(0)
semC2 = mp.Semaphore(0)

Q1 = mp.Queue()
Q2 = mp.Queue()

def P1(N):
    for i in range(N):
        semQ1.acquire()
        val = rd.randint(0,9)
        Q1.put(val)
    sys.exit(0)

def P2(N):
    for i in range(N):
        semQ2.acquire()
        val = rd.randint(0,9)
        Q2.put(val)
    sys.exit(0)
    
def C1(N):
    for i in range(N):
        semC2.release()
        val = Q1.get()
        semQ1.release()
        print("C1",val)
        semC1.acquire()

def C2(N):
    for i in range(N):
        semC2.acquire()
        val = Q2.get()
        semQ2.release()
        print("C2",val)
        semC1.release()



P1 = mp.Process(target = P1, args = (N,))
P2 = mp.Process(target = P2, args = (N,))
C1 = mp.Process(target = C1, args = (N,))
C2 = mp.Process(target = C2, args = (N,))


P1.start()
P2.start()
C1.start()
C2.start()

P1.join()
P2.join()
C1.join()
C2.join()

sys.exit(0)