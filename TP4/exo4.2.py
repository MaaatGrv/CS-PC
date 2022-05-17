# 17.05.22
# @Mathis Gorvien

import sys
import multiprocessing as mp

semP1 = mp.Semaphore(0)
semP2 = mp.Semaphore(0)
semP3 = mp.Semaphore(0)

def fP1():
    print("Je suis P1")
    print("P1 finito")
    semP2.release()
    semP3.release()
    semP1.acquire()
    semP1.acquire()
    rdv1()
    sys.exit(0)

def fP2():
    print("Je suis P2")
    print("P2 finito")
    semP1.release()
    semP3.release()
    semP2.acquire()
    semP2.acquire()
    rdv2()
    sys.exit(0)

def fP3():
    print("Je suis P3")
    print("P3 finito")
    semP1.release()
    semP2.release()
    semP3.acquire()
    semP3.acquire()
    rdv3()
    sys.exit(0)

def rdv1():
    print("Je suis le rdv 1")

def rdv2():
    print("Je suis le rdv 2")

def rdv3():
    print("Je suis le rdv 3")

P1 = mp.Process(target = fP1, args = ())
P2 = mp.Process(target = fP2, args = ())
P3 = mp.Process(target = fP3, args = ())

P1.start()
P2.start()
P3.start()

P1.join()
P2.join()
P3.join()

sys.exit(0)