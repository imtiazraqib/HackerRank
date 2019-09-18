# Enter your code here. Read input from STDIN. Print output to STDOUT

testCases = int(input())

for i in range(testCases):

    word = input()

    for j in range(len(word)):
        if j%2 == 0:
            print(word[j], end='')

    print(" ", end="")

    for j in range(len(word)):
        if j%2 !=0 :
            print(word[j], end='')

    print('')