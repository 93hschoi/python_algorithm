list_ap = []
case = int(input())
num = 0

def sum(a,b):
    result = 0
    for l in range(0,b):
        result += list_ap[a-1][l]
    return result

for z in range(case):
    k = int(input())
    n = int(input())
    list_ap = [[0 for _ in range(1,n+1)] for _ in range(0,k+1)]
                #주의!!. 여기서 range안의 의미는 "갯수"만 세고, 결국 0번째부터 시작함

    for i in range(0,k+1):
        for j in range(0,n):   #따라서 여기서 1부터 시작하면, 배열에 안맞음.
            if( i == 0 ):
                list_ap[i][j] = j+1
            else:
                list_ap[i][j] = sum(i,j+1)

    print(list_ap)
    print(list_ap[k][n-1])