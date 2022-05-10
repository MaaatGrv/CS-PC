import sys, os
for i in range(3):
    pid=os.fork()
    if pid==0:
        print("i :",i,"je suis le processus",os.getpid(),"mon père est",os.getppid())
        sys.exit(0)

#                         Père 3124
#                      /      !      \
#                     /       !       \
#                  Fils0    Fils1    FILS2

