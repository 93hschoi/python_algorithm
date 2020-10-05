n = int(input())
fibo_list = [0,1]

for i in range(2,n+1):
    a = fibo_list[i-1]+fibo_list[i-2]
    fibo_list.append(a)

print(fibo_list[n])
