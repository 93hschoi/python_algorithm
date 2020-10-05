case = int(input())
result = 0

for i in range(case):
    H,W,N = map(int,input().split())
    cus_list = []
    room = 0
    for j in range(1, W + 1):
        for k in range(1, H + 1):
            room = 100 * k + j
            cus_list.append(room)
            if(N == len(cus_list)):
                result = cus_list[N - 1]

    print(result)