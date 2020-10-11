n = int(input())
list = [0,1]

for i in range(2,n+1):
    a = list[i-1] + list[i-2]
    list.append(a)

print(list[n])