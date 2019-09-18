import math
import os
import random
import re
import sys

def listReversal(index, array):
    array.reverse()

    for i in range(0, index):
        print(array[i], end=' ')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    listReversal(n, arr)