import sys

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

sys.exit(0)