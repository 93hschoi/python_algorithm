N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))

for i in range(1,len(num_list)):
    j = i-1
    key = num_list[i]
    while num_list[j] > key and j >=0:
        num_list[j+1] = num_list[j]
        j = j-1
    num_list[j+1] = key

print(num_list)

