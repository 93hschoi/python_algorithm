N = int(input())
weight_list = []
height_list = []
rank_list = [1]*N

for n in range(N):
    x , y = map(int, input().split())
    weight_list.append(x)
    height_list.append(y)

for i in range(0,N):
    for j in range(0,N):
        if(weight_list[i]<weight_list[j] and height_list[i]<height_list[j]):
            rank_list[i]+=1


print(rank_list)