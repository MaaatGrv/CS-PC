import sys

def moyenne(list_of_notes):
    S=0
    N=len(list_of_notes)
    for note in list_of_notes:
        S+=note
    return(S/N)

list_of_notes=[]
moy=""
pb=0

if len(sys.argv)-1 == 0:
    print("Aucune moyenne à calculer")

else:
    for arg in sys.argv[1:]:
        try :
            note=float(arg)
        except :
            print("Note(s) non valide(s)")
            exit()
        if note >= 0 and note <= 20 :
            list_of_notes.append(note)
        else:
            pb=1
    if pb==1 :
        print("Note(s) non valide(s)")
    else:
        moy=moyenne(list_of_notes)
        print("Moyenne est :", "%.2f" %moy)