from colorama import Fore
from functools import cache
from pathlib import Path
import sys

sys.setrecursionlimit(2100)

example = False  # True  #

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

prices = [int(p) for p in open(file).read().split('\n')]


def mix(secret, new):   #bitwise xor
    return secret ^ new

def prune(secret):
    return secret % 16777216

def times64(secret):
    return prune(mix(secret*64, secret))

def divide32(secret):
    return prune(mix(secret//32, secret))

def times2048(secret):
    return prune(mix(secret*2048, secret))

@cache
def calcPrices(price, rec):
    if rec == 0: return price
    return calcPrices(
        times2048(divide32(times64(price))), 
        rec-1)

score = sum(calcPrices(calcPrices(price, 1000),1000) for price in prices)
print(score)

# price=123
# for i in range(10):
#     price = times2048(divide32(times64(price)))
#     print(price)

# example:  37327623 # 
# input:    15608699004 # spot on