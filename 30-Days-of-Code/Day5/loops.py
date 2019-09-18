import math
import os
import random
import re
import sys

def test(n):
    for i in range(1, 11):
        a = n * i
        print(str(n) + " x " + str(i) + " = " + str(a))

if __name__ == '__main__':
    n = int(input())
    test(n)