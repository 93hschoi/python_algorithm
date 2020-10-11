T = int(input())
num_list = [1,1,1,2,2]

for _ in range(T):
    N = int(input())

    if (N <= 5):
        print(num_list[N-1])
        num_list = [1, 1, 1, 2, 2]   #초기화 시켜주지 않으면 계속해서 다른리스트로 변함
    else:
        for i in range(N - 1):
            s = num_list[i] + num_list[i+4]
            num_list.append(s)
        print(num_list[N-1])
        num_list = [1, 1, 1, 2, 2]




