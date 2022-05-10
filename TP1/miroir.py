import sys
word = sys.argv[1]
list_of_letters = list(word)
new = "" 
for i in range(0,len(list_of_letters)):
    new += list_of_letters[-1-i]
print(new)