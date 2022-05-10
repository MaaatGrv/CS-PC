import os,sys

dicoNotes = { "E1" : [10, 15, 20], "E2" : [12, 16, 15], "E3" : [11, 13, 20], "E4" : [19, 13, 20], "E5" : [17, 13, 10], "E6" : [13, 13, 12], "E7" : [10, 13, 13]}

nb_eleves=len(dicoNotes)

max=0
prems=""

min=20
cancre=""

print("")

for eleve in dicoNotes :
    moy=0
    liste_notes=dicoNotes[eleve]
    for note in liste_notes :
        moy+=note
    moy=moy/len(liste_notes)
    print("L'élève", eleve, "a obtenu", "%.2f" %moy, "de moyenne")

    if moy > max :
        max=moy
        prems=eleve
    
    if moy < min :
        min=moy
        cancre=eleve

print("")
print("Félicitations élève", prems, ", tu es premier de la classe! Continue comme ça, c'est super!")
print("")
print("Attention élève", cancre, ", tu es dernier de la classe! Tu dois te mettre au travail!")
print("")