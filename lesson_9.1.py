import time
import sys
from time import sleep

class TrafficLight():
    # attribute class

    # attribute object
    def __init__(self):
        self.__color = ('red', 'yellow', 'green')

    # method
    def running(self):
        for c in self.__color:
            if c == 'red':
                print("\033[31m{}".format(c), end='')
                print("\033[0m")
                time.sleep(7)
            elif c == 'yellow':
                print("\033[33m{}".format(c), end='')
                print("\033[0m")
                time.sleep(2)
            else:
                print("\033[32m{}".format(c), end='')
                print("\033[0m")
                time.sleep(5)


svetofor = TrafficLight()
while True:
    svetofor.running()
