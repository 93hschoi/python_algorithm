N, M = map(int, input().split())
ans_list = []

def combination(count):
    if(count == M):
        print(ans_list)
        return

    for i in range(1,N+1):
        ans_list.append(i)
        combination(count+1)
        ans_list.remove(i)


combination(0)