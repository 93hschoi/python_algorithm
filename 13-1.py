N,M = map(int,input().split())
cards_list = list(map(int, input().split()))
sum_list = []
max_sum=0

for i in range(1,len(cards_list)-2):
    for j in range(i+1,len(cards_list)-1):
        for n in range(j+1, len(cards_list)):
            sum = cards_list[i]+cards_list[j]+cards_list[n]
            if(sum <= M):
                sum_list.append(sum)
                sum_list.sort()
                max_sum = max(sum_list)


print(max_sum)



