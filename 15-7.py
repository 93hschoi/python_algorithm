N = int(input())
numbers = list(map(int, input().split()))
cal_number = list(map(int, input().split()))
sol_list = []

def change(a,b):
    if(a<0):
        return -1*(-1*a//b)
    else:
        return a//b

def calculation(ans,count):

    if(count == len(numbers)-1):
        sol_list.append(ans)
        return

    next = count + 1
    last = ans

    for i in range(4):
        if(i == 0):
            if(cal_number[i] != 0):
                ans = ans + numbers[next]
                cal_number[i] = cal_number[i] - 1
                calculation(ans,count + 1)
                ans = last
                cal_number[i] = cal_number[i] + 1
        if(i == 1):
            if (cal_number[i] != 0):
                ans = ans - numbers[next]
                cal_number[i] = cal_number[i] - 1
                calculation(ans,count + 1)
                ans = last
                cal_number[i] = cal_number[i] + 1
        if(i == 2):
            if (cal_number[i] != 0):
                ans = ans * numbers[next]
                cal_number[i] = cal_number[i] - 1
                calculation(ans,count + 1)
                ans = last
                cal_number[i] = cal_number[i] + 1
        if(i == 3):
            if (cal_number[i] != 0):
                ans = change(ans,numbers[next])
                cal_number[i] = cal_number[i] - 1
                calculation(ans,count + 1)
                ans = last
                cal_number[i] = cal_number[i] + 1


calculation(numbers[0],0)

print(max(sol_list))
print(min(sol_list))
