from pathlib import Path
from colorama import Fore

import re

example = True  #False  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

caluculations = []
for l in open(file).readlines():
    result, operands = l.strip().split(': ')
    operands = operands.split(' ')
    operator = [[['+'], ['*']]]

    print(l.strip())
    print(operands, len(operands))
    num_operators = len(operands)-1
    
    # '{0:07b}'.format(12) 2^num_operators

    if num_operators > 1:
        for i in range(num_operators):
            for j, o in enumerate(operator[i]):
                # print(i, operator[i][j])
                operator.append([['+'], ['*']])     #operator[i][j].append('+'), operator[i][j].append('*')

            # print(i,'o' ,o)
            # t = [o.append('+'), o.append('*')]
            # # operator.append(t)
            # print(i,'t' , t)
            for o in operator:
                print(i, o)

    # print(operator)
    input()

    # dic = {'result': result,
    #        'operands': operands,
    #        'operator': operator,
    #        }
    
    # caluculations.append(dic)



lines = [l.strip() ]














checksum = 0


print('Anser: ', checksum) 

assert checksum == 2858 if example else 6412390114238
