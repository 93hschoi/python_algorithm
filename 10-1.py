N = int(input())
list_num = list(map(int, input().split()))
prime_number = False
num = 0

def prime(k):
    if(k == 1):
        return False
    for i in range(2,k):
        if(k % i ==0):
            return False

    return True

for i in range(len(list_num)):
    check = list_num[i]
    if(prime(check) == True):
        num +=1

print(num)
