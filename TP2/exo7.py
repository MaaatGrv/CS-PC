import os,sys

N=3
for i in range(N) :
    #__________début des ajouts_________
    if os.fork():
        if os.fork():
            os.fork()
    # __________fin des ajouts__________
print("Bonjour")
sys.exit(0)