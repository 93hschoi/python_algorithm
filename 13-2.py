N = int(input())
M_list = []

for i in range(1,N):
    a = i//100
    b = i//10 -a*10
    c = i%10
    M = i+a+b+c
    if(M ==N):
        M_list.append(i)

print(min(M_list))



