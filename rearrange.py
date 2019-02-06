# completed multiple ways without shuffle, now using fisher-yates

import random
import sys
import random

words = sys.argv[1:]
neworder = []
# randintlist = []

# while len(neworder) < len(words):
#     num =  random.randint(0,len(words)-1)
#     if len(randintlist) == 0:
#         neworder.append(words[num])
#         randintlist.append(num)
#     elif num not in randintlist:
#         neworder.append(words[num])
#         randintlist.append(num)
#
# print(*neworder)

# length=len(words)
# for i in range(length):
#     num = random.randint(0, len(words)-1)
#     neworder.append(words[num])
#     del words[num]

def fisher_yates_shuffle(words):
    amntToShuffle = len(words)
    while amntToShuffle > 1:
        i = int(floor(random()))



print(*neworder)
