import os, sys

(dfr,dfw) = os.pipe()
(dfr2,dfw2) = os.pipe()
pid = os.fork()
fichier = os.open("sortie.txt",os.O_CREAT|os.O_WRONLY,0o0644)
lecture = os.open("fichier_trie.txt",os.O_CREAT|os.O_RDONLY,0o0644)

if pid==0:
    os.close(dfr)
    os.close(dfw2)
    os.close(dfr2)
    os.dup2(dfw,1)
    os.dup2(lecture,0)
    os.close(dfw)
    os.execlp("sort", "sort")

else : 
    pid = os.fork()
    if pid==0:
        os.close(dfw)
        os.close(dfr2)
        os.dup2(dfr,0)
        os.dup2(dfw2,1)
        os.close(dfr)
        os.close(dfw2)
        os.execlp("grep","grep","chaine")
    else : 
        os.close(dfw)
        os.close(dfr)
        os.close(dfw2)
        os.dup2(dfr2,0)
        os.dup2(fichier,1)
        os.close(dfr2)
        os.execlp("tail","tail","-n","5")

sys.exit(0)