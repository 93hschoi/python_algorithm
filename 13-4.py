N, M = map(int, input().split())
eight_list = []
row_list = []
result_list=[]
string=""
for _ in range(N):
    row_list.append(input())

def check():
    row_num = 0

    for i in range(1,8):
        before=eight_list[i-1][0]
        now=eight_list[i][0]
        if (before == now):
            if (now == "W"):
                eight_list[i][0] = "B"
            else:
                eight_list[i][0] = "W"
            row_num += 1

    for i in range(8):
        for j in range(1,8):
            before = eight_list[i][j-1]
            now = eight_list[i][j]
            if(before == now):
                if(now=="W"):
                    eight_list[i][j]="B"
                else:
                    eight_list[i][j]="W"
                row_num+=1

    result_list.append(row_num)


for a in range(N-7):
    for b in range(M-7):
        for i in range(a,a+8):
            for j in range(b, b+8):
                string=string+row_list[i][j]
            eight_list.append(list(string))
            string=""
        check()

        eight_list=[]
print(min(result_list))

