N,M = map(int,input().split())
cards_list = list(map(int, input().split()))
sum=0
result_list=[]
def func(count,k):
    global sum
    if(count>3):
        if(sum<=M):
            result_list.append(sum)
        return
    else:
        for i in range(k,len(cards_list)-(3-count)):
            sum+=cards_list[i]
            func(count+1,i+1)
            sum-=cards_list[i]
func(1,0)
print(max(result_list))

