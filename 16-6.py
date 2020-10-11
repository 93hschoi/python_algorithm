N = int(input())
sum_list = []
pyramid = []

for _ in range(N):
    line = list(map(int,input().split()))
    pyramid.append(line)

for n in range(N):
    sum_list.append(pyramid[N-1][n])

for n in range(N-1, 0,-1):   #4,3,2,1
    for i in range(len(pyramid[n])):
        if(i == 0):
            sum_list[0] += pyramid[n-1][0]
        else:
            if(pyramid[n-1][i-1]>pyramid[n-1][i]):
                sum_list[i] += pyramid[n-1][i-1]
            else:
                sum_list[i] += pyramid[n-1][i]

print(min(sum_list))
