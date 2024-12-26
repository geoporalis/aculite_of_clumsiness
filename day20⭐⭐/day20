from pathlib import Path

example = False # True #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

start, end = (), ()
area = []
for x, l in enumerate(open(file).readlines()):
    line = []
    for y, c in enumerate(l.strip('\n')):
        if c == 'S':
            start = (x,y)
            c = '.'
        if c == 'E':
            end = (x,y)
            c = '.'
        line.append(c)
    area.append(line)

todo = [(start)]

for (x,y) in todo:
    for dx,dy in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
        if not (dx,dy) in todo:
            if area[dx][dy] == '.':
                todo.append((dx,dy))

print('track length', len(todo))
part1 = part2 = 0
for i, short in enumerate(todo[:]):         # -1
    for j, cut in enumerate(todo[:]):       # i+1
        diff = abs(short[0]-cut[0]) + abs(short[1]-cut[1])
        if diff == 2 and (j-i-diff) >= 100: part1+=1
        if diff < 21 and (j-i-diff) >= 100: part2+=1
    print('\r',part1, part2, end='')    

# example:  0
# input:    5433 # too high

# crazy: 1502 # 1028136  ?manhatten distance?
