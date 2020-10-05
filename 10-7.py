a_list = []
b_list = []
first = 0
second = 0

for i in range(3):
    a,b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for j in range(len(a_list)):
    if(a_list.count(a_list[j])==1):
        first = a_list[j]

for n in range(len(b_list)):
    if(b_list.count(b_list[n])==1):
        second = b_list[n]

print(first, second)
