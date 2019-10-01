import math
import os
import random
import re
import sys

def hourGlass(arr):

    maxSum = -9999999
    computedSum = 0

    for i in range(len(arr)-1):
        for j in range(len(arr)-1):

            if ((i+2) < len(arr) and (j+2) < len(arr)):
                computedSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            if maxSum < computedSum:
                maxSum = computedSum

    print(maxSum)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourGlass(arr)
