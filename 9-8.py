T = int(input())
num_list = []
num = 0

for i in range(1,1000):
    if (i % 2 == 1):
        num = i // 2 + 1
    else:
        num = i // 2
    for j in range(num):
        num_list.append(i)

for z in range(T):
    x, y = map(int, input().split())
    leng = y - x

    print(num_list[leng-1])


