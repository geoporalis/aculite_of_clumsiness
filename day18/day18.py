import re
from pathlib import Path

example = False # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

(height, width) = (7, 7) if example else (71, 71)

limit = 11 if example else 1023

grid = {(x,y):'.' for x in range(height) for y in range(width)}

pyts =  { grid.pop(tuple([*map(int,re.findall(r'-?\d+',l))])) for l in open(file).readlines()[:limit]}

for y in range(height):
    for x in range(width):
            if (x,y) in grid:
                print(' ',end='')
            else:
                print('#',end='')
            # print(',',end='')    
    print()
# bots = [[*map(int, re.findall(r'-?\d+',l))]
                #    for l in open(file)]
# print(grid)