N = int(input())
strnum_list = []

for _ in range(N):
    string = input()
    strnum_list.append(string)


strnum_list = list(set(strnum_list))
strnum_list.sort(key = lambda x: len(x))

for j in range(len(strnum_list)-1):
    for i in range(len(strnum_list) - 1 -j):

        if (len(strnum_list[i]) == len(strnum_list[i + 1])):
            if (strnum_list[i] > strnum_list[i + 1]):
                temp = strnum_list[i]
                strnum_list[i] = strnum_list[i + 1]
                strnum_list[i + 1] = temp

print(strnum_list)