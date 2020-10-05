N, M = map(int, input().split())
ans_list = []
check_list = [False]*(N+1)

def sortion(count,last):
    if(count == M):
        print(ans_list)
        return

    for i in range(last, N+1):
        if(check_list[i] == False):
            ans_list.append(i)
            check_list[i] = True
            sortion(count+1,i+1)
            ans_list.remove(i)
            check_list[i] = False

sortion(0,1)