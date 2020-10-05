N = int(input())
num_list = []
list_count = []
second_list = []

for _ in range(N):
    num_list.append(int(input()))

# 산술평균
sansul_average = round(sum(num_list)/N)
num_list.sort()
print(sansul_average)

# 중앙값
center = len(num_list)//2
center_average = num_list[center]
print(center_average)

#최빈값
k=0
for i in range(len(num_list)):
    if(i+k>=len(num_list)):
        break
    list_count.append([num_list[i+k], num_list.count(num_list[i+k])])
    k = num_list.count(num_list[i+k])-1

list_count.sort(key = lambda x: x[1])
largest = list_count[len(list_count)-1][1]
for i in range(len(list_count)):
    if(list_count[i][1]==largest):
        second_list.append(list_count[i][0])

if(len(second_list)==1):
    print(second_list[0])
else:
    print(second_list[1])

#범위
range = max(num_list) - min(num_list)
print(range)