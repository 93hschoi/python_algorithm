N = int(input())
house_list = []
RGB_check = [False]*N

for i in range(N):
    RGB_LIST = list(map(int, input().split()))
    house_list.append(RGB_LIST)

s= 0
s_list = []
def choice(count):
    global s
    if(count == N):
        s_list.append(s)
        return

    for i in range(0, 3):
        if (RGB_check[i] == False):
            if (i == 0):
                s += house_list[count][i]
                RGB_check[i] = True
                RGB_check[1] = False
                RGB_check[2] = False
                choice(count + 1)
                RGB_check[i] = False
                s -= house_list[count][i]
            if (i == 1):
                s += house_list[count][i]
                RGB_check[i] = True
                RGB_check[0] = False
                RGB_check[2] = False
                choice(count + 1)
                RGB_check[i] = False
                s -= house_list[count][i]
            if (i == 2):
                s += house_list[count][i]
                RGB_check[i] = True
                RGB_check[1] = False
                RGB_check[0] = False
                choice(count + 1)
                RGB_check[i] = False
                s -= house_list[count][i]

choice(0)
print(min(s_list))


