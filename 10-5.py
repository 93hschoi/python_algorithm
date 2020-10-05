T = int(input())

def prime(k):
    if(k==1):
        return False
    for i in range(2,k):
        if(k % i ==0):
            return False
    return True

for t in range(T):
    n = int(input())
    prime_list = []
    diff_list = []

    for i in range(2,n):
        if(prime(i) == True):
            prime_list.append(i)

    for j in range(len(prime_list)):
        x = prime_list[j]
        y = n - x
        if(y in prime_list):
            diff_list.append(x)

    if(len(diff_list) % 2 ==0):
         a = len(diff_list)//2
         print(diff_list[a-1],diff_list[a])
    else:
         a = len(diff_list)//2+1
         print(diff_list[a-1],diff_list[a-1])





