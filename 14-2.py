N = int(input())
num_list = []
num_list1 = ''
num_list2 = ''
for i in range(N):
    num_list.append(int(input()))

def sort():
    global num_list1, num_list2
    while(True):
        num_list1 ="".join(map(str,num_list))

        for i in range(N - 1):
            if (num_list[i] > num_list[i + 1]):
                temp = num_list[i + 1]
                num_list[i + 1] = num_list[i]
                num_list[i] = temp

        num_list2 = "".join(map(str,num_list))
        if(num_list1 == num_list2):
            for j in range(N):
                print(num_list2[j])
            break
        else:
            num_list1 = num_list2

sort()
