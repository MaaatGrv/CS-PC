import sys,os,time

N = int(sys.argv[1])

for i in range(1,N+1):
    fils=os.fork()
    if fils==0:
        print("")
        print("i :",i,"je suis le processus",os.getpid(),"mon père est",os.getppid())

        print("dodo...Zzzz")
        time.sleep(2*i)

        sys.exit(i)
    
    pid_fils,etat=os.wait()

    print(pid_fils, os.WEXITSTATUS(etat))
