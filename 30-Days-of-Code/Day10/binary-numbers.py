import math
import os
import random
import re
import sys

def countBinaryOnes(n):

    # Converting number to binary
    # Python's bin functions returns binary starting with '0b'
    # [2:] removes the first two characters of the string
    binary_n = str(bin(n))[2:]

    countOnes = 0
    consecOnes = 0
    
    for i in range(len(binary_n)):
        if binary_n[i] == '0':
            countOnes = 0
        else:
            countOnes += 1
            consecOnes = max(consecOnes, countOnes)
            
    print(consecOnes)

if __name__ == '__main__':
    n = int(input())
    countBinaryOnes(n)
