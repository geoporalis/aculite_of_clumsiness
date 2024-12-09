from pathlib import Path
from colorama import Fore

import re

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() 
# file = Path(dir/'example').resolve()

oneline = open(file).read()   #.strip()


id=0
newline=""
for idx in range(1,len(oneline)+1,2):
    newline += str(id)*int(oneline[idx-1])
    try:
        newline += '.'*int(oneline[idx])
    except:
        pass
    id+=1

newlist = list(newline)
print("".join(newlist))
new_len = len(newlist)
point_idx = [i for i in range(new_len) if newline[i] == '.']
num_idx = [i for i in range(new_len) if newline[i] != '.']

while True:
    j = point_idx.pop(0)
    i = num_idx.pop(-1)
    if i < j:
        break
    newlist[i], newlist[j] = newlist[j], newlist[i]
    print('\r', new_len,'/', i,'/', j, end='')
    
print()
print("".join(newlist))
checksum = 0
idx = 0
while True:
    checksum += int(newlist[idx])*idx
    idx+=1
    if newlist[idx] == '.':
        break

print(checksum) 
# 90967962125 # too low
# 90994085674 # still too low

# example = 1928 // 1928
