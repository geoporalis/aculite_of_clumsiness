import re, math
from colorama import Fore
from pathlib import Path

example = True  #False  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

pattern = r'p=(\d{1,}),(\d{1,})\sv=(-?\d{1,}),(-?\d{1,})'

margin = 10000000000000
robots = [ {'px': int(claw[0]), 'py': int(claw[1]),
           'dx': int(claw[2]), 'dy': int(claw[3]),
           } for claw in re.findall(pattern, open(file).read())]

# print(robots)
w = 11 if example else 101 # x-axis
h = 7 if example else 103 # y-axis

wq = w//2
wm = w-wq-1
hq = h//2
hm = h-hq-1

print(wq, wm,'||', hq, hm)

def getQuadrant(nx, ny):
    if nx == (wm) or ny == (hm):
        return 0  
    q = 1 if nx < wm else 2
    q += 2 if ny > hm else 0
        
    return q        

def moveRobot(robot, seconds):#%w, \
    nx, ny =    (robot['px'] + robot['dx']*seconds), (robot['py'] + robot['dy']*seconds) #%h

    if nx >= 0:
        nx = nx%w
    else:
        nx = w- ( nx%w)
        # print('x:', nx, nx%w, nx//w)

    if ny >= 0:
        ny = ny%h
    else:
        ny = h-(ny%h)
        # print('y:',ny, ny%h, ny//h)

    # nx = nx%w if nx >= 0 else nx - ((nx//w))*w
    # ny = ny%h if ny >= 0 else ny - ((ny//h))*h
    
    cx = Fore.RED if nx == wm else Fore.RESET
    cy = Fore.RED if ny == hm else Fore.RESET

    print(cx, nx, cy, ny, Fore.RESET )


    nx += w if nx < 0 else 0
    ny += h if ny < 0 else 0

    return getQuadrant(nx, ny)

after100s = [moveRobot(robot, 100) for robot in robots]

quads100s = [after100s.count(i) for i in range(0,5)]

print(quads100s, math.prod(quads100s[1:]))
# p=
# \sv=(\d{1,})
# 