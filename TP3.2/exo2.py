import sys, signal,time


def end(signal,frame):
    print("SIGINT pour processus")


signal.signal(signal.SIGINT,end)
while True:
    print('Hello')
    time.sleep(2)