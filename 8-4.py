case = int(input())

for i in range(case):
    num ,S= input().split()
    for j in range(len(S)):
        print(S[j]*int(num), end='')

    print()

