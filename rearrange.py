import random
import sys

words = sys.argv[1:]
neworder = []
randintlist = []

while len(neworder) < len(words):
    num =  random.randint(0,len(words)-1)
    if len(randintlist) == 0:
        neworder.append(words[num])
    elif num not in randintlist:
        neworder.append(words(num))

print(*neworder)
