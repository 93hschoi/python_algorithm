A, B, V = map(int, input().split())
height = 0
day = 0

for i in range(1,10):
    height += A
    if(height == 5):
        day = i
        break
    else:
        height -= B

print(day)