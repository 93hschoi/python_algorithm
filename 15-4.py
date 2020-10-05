N, M = map(int, input().split())
ans_list = []

def combination(count,last):
    if(count == M):
        print(ans_list)
        return

    for i in range(last,N+1):
        ans_list.append(i)
        combination(count+1,i)
        ans_list.remove(i)


combination(0,1)