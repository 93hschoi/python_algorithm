N, M = map(int, input().split())
ans_list = []
check_list = [False]*(N+1)

def sortion(count):
    if(count == M):
        print(ans_list)
        return

    for i in range(1, N+1):
        if(check_list[i] == False):
            if(count >=1):
                if(ans_list[count-1] < i):
                    ans_list.append(i)
                    check_list[i] = True
                    sortion(count + 1)
                    ans_list.remove(i)
                    check_list[i] = False
            else:
                ans_list.append(i)
                check_list[i] = True
                sortion(count + 1)
                ans_list.remove(i)
                check_list[i] = False

sortion(0)