import sys, signal,time

fin=False
def end(signal,frame):
    global fin
    print("SIGINT pour processus")
    fin=True


signal.signal(signal.SIGINT,end)
while not fin:
    print('Hello')
    time.sleep(2)