sudoku =[]
for _ in range(9):
    line = list(map(int, input().split()))
    sudoku.append(line)
#스도쿠 입력받음


def row_check(y,k):
    if(k in sudoku[y]):
        return False
    return True

def column_check(x,k):
    for i in range(9):
        if(sudoku[i][x] == k):
            return False
    return True

def square_check(y,x,k):
    for i in range(y,y+3):
        for j in range(x, x+3):
            if(sudoku[i][j]==k):
                return False
    return True


def solution(count):
    if(count == 81):
        print(sudoku)
        return

    y = count//9
    x = count%9
    if(sudoku[y][x] ==0):
            for i in range(1,10):
                if(row_check(y,i) and column_check(x,i)and square_check(y//3*3,x//3*3,i) ):
                    sudoku[y][x] = i
                    solution(count+1)
                    sudoku[y][x] = 0
    else:
        solution(count+1)

solution(0)





