import sys

def reverse_by_m(word):
    list_of_letters = list(word)
    new = "" 
    for i in range(0,len(list_of_letters)):
        new += list_of_letters[-1-i]
    return(new)

for arg in sys.argv[1:]:
    print(reverse_by_m(arg))