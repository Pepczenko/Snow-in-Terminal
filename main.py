from random import randint
from time import sleep
import sys

sys.setrecursionlimit(100000000)
def conversion(numberOfSpaces):
    oneSpace = ' '
    convergedspaces = ''.join(oneSpace * numberOfSpaces)
    
    return convergedspaces

def loop():
    direction = +1
    spaces = 0

    while True:
        
        print(conversion(spaces) + '*')
        spaces += direction
        sleep(.05)
        if spaces == 10:
            direction = -1
        if spaces == 0:
            loop()
loop()