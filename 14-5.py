N = int(input())
num_list = []
ans_list = []

a = str(N)
for i in a:
    b = int(i)
    num_list.append(b)

num_list.sort()


for i in range(len(num_list)-1,-1,-1):
    ans_list.append(num_list[i])

answer = ''.join(map(str,ans_list))
print(answer)