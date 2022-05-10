import multiprocessing as mp 
import os , sys

T = (100,200,300)
(dfr,dfw) = mp.Pipe( )
pid = os.fork( )
if pid != 0 : #Processus PERE
    dfr.close( )
    n = dfw.send(T)
    print ("Le FILS %d a transmis le message %s\n" %(os.getpid(),T))
    dfw.close( )
else : #Processus FILS
    dfw.close( )
    msgReception = dfr.recv( )
    print ("Le PERE %d a reçu le message %s\n" %(os.getpid(),msgReception)) 
    dfr.close( )
sys.exit(0)
