import re, math
from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pattern = r'p=(\d{1,}),(\d{1,})\sv=(-?\d{1,}),(-?\d{1,})'

margin = 10000000000000
robots = [ {'px': int(claw[0]), 'py': int(claw[1]),
           'dx': int(claw[2]), 'dy': int(claw[3]),
           } for claw in re.findall(pattern, open(file).read())]

w = 11 if example else 101 # x-axis
h = 7 if example else 103 # y-axis

wq = w//2
wm = w-wq-1
hq = h//2
hm = h-hq-1

# print(wq, wm,'||', hq, hm)

def getQuadrant(nx, ny):
    if nx == (wm) or ny == (hm):
        return 0  
    q = 1 if nx < wm else 2
    q += 2 if ny > hm else 0
        
    return q        

def moveRobot(robot, seconds):#%w, \
    nx, ny =    (robot['px'] + robot['dx']*seconds), (robot['py'] + robot['dy']*seconds) #%h

    while nx < 0: nx += w
    nx = nx%w

    while ny < 0: ny += h
    ny = ny%h

    return (nx, ny) # (nx, nx, )  #getQuadrant
# part 02


# secFac = []
# minsf = 42229965120
# for i in range(7500, 9800):
#     # quads = []
#     # for r, robot in enumerate(robots):
#     #     # robots[r]['px'], robots[r]['py'], 
#     #     q = moveRobot(robot, i)
#     #     quads.append(q)
#     quads = [moveRobot(robot, i)  for robot in robots]    
#     csf = [quads.count(j) for j in range(0,5)]
#     sf = math.prod(csf[1:])

# #     # print(i, csf, sf)
#     if sf < 56000000 and sf != 0:
#         minsf = sf
#         print(i, sf)
#         secFac.append((sf, i))

getAll = set()
for robot in robots:
    getAll.add(moveRobot(robot, 8179))
for y in range(h):
    for x in range(w):
    
        if (x,y) in getAll:
            print("#",end='')
        else:
            print(" ",end='')
    print()

# 8886
# 8179
'''
7500 213104520
7520 210396160
7561 204141168
7573 55572125
7674 54832668
7775 53100180
7876 48871872
8583 47833200
8886 46516005
'''
                                          #            #                                              #
# quads100s = [after100s.count(i) for i in range(0,5)]

# print(quads100s, math.prod(quads100s[1:]))


# part 02
# ?variance 
# ?chinese remainder theroem

# for s in range(7500, 8800):
#     moved = [moveRobot(robot, s) for robot in robots]
#     count = [moved.count(i)      for i in range(0,5)]
#     if math.prod(count) == 0:
#         print(s, count)
#         input()
#     print('\r', s, end='')

# p=
# \sv=(\d{1,})
# 