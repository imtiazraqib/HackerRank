# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

phoneBook = dict()
num_entries = int(input())

for i in range(num_entries):
    
    entry = input()
    entry = entry.split(" ")
    phoneBook[entry[0]] = entry[1]

queries = stdin.read().splitlines()
for i in range(len(queries)):
    if queries[i] in phoneBook:
        print("%s=%s" % (queries[i], phoneBook[queries[i]]))
    else:
        print("Not found")