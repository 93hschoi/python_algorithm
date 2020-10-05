N = int(input())
num_list = []

for i in range(N):
    a, b = map(str, input().split())
    c = int(a)
    num_list.append([c,b,i])

num_list.sort(key =  lambda x: x[0])
for m in range(N):
    for n in range(N - 1):
        if (num_list[n][0] == num_list[n + 1][0]):
            if (num_list[n][2] > num_list[n + 1][2]):
                temp = num_list[n][1]
                num_list[n][1] = num_list[n + 1][1]
                num_list[n + 1][1] = temp

for i in range(N):
    print(num_list[i][0], num_list[i][1])

