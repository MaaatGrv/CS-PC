import sys, signal,time


def end(signal,frame):
    print("SIGINT pour processus")
    sys.exit(0)

signal.signal(signal.SIGINT,end)
while True:
    print('Hello')
    time.sleep(2)
