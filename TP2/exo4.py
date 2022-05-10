import os,sys
n=0
for i in range(1,5) :
    if os.fork():
        if os.fork():
            os.fork()
print("n = ", n) #4
sys.exit(0)

#Réponses aux questions
#
#Le programme est déterministe
