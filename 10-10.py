import math
T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    ex_length = r1+r2
    if(x1==x2 and y1 ==y2):
        print(0)
    else:
        if (length < ex_length):
            print(2)
        elif (length == ex_length):
            print(1)
        else:
            print(0)
