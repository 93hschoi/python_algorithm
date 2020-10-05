N = int(input())
chess_list = []
result = 0

for n in range(N):
    chess_list.append([False]*10)

def check(y,x):
    for i in range(1,y+1):
        if(chess_list[i-1][x] == True):
            return False
        if(0 <= x+i < N):
            if(chess_list[y-i][x+i] ==True):
                return False
        if(0 <= x-i < N):
            if(chess_list[y-i][x-i] == True):
                return False
    return True

def chess(count):
    global result
    if(count == N):
        result+=1
        return

    for i in range(N):
        if(chess_list[count][i] == False):
            if(check(count,i) == True):
                chess_list[count][i] = True
                chess(count+1)
                chess_list[count][i] = False

chess(0)
print(result)

