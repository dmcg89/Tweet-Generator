import random
import sys

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

length=len(words)
for i in range(length):
    num = random.randint(0, len(words)-1)
    neworder.append(words[num])
    words.pop(num)

print(*neworder)
