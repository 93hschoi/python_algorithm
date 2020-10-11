N = int(input())
check_N = [False]*(N)
M = int(N/2)
arr = []
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
team_sum = 0
start_team = []
start_team_sum_list = []
link_team_sum_list = []
diff_list = []

def sum_sym(a,b):
    global team_sum
    team_sum = arr[a][b] + arr[b][a]
    return team_sum

def choice_sum(count):
    if(count == M):
        start_team_sum=[]
        link_team_sum=[]
        link_team=[]
        for i in range(len(start_team)):
            for j in range(i,len(start_team)):
                start_team_sum.append(sum_sym(start_team[i],start_team[j]))

        for i in range(N):
            if(check_N[i] == False):
                link_team.append(i)

        for i in range(len(link_team)):
            for j in range(i,len(link_team)):
                link_team_sum.append(sum_sym(link_team[i],link_team[j]))

        start_team_sum_list.append(sum(start_team_sum))
        link_team_sum_list.append(sum(link_team_sum))

        return

    for i in range(N):
        if(check_N[i] == False):
            start_team.append(i)
            check_N[i] = True
            choice_sum(count+1)
            check_N[i] = False
            start_team.remove(i)


choice_sum(0)

for p in range(len(start_team_sum_list)):
    diff = start_team_sum_list[p] - link_team_sum_list[p]
    if(diff < 0):
        diff = -(diff)
    diff_list.append(diff)


print(min(diff_list))
