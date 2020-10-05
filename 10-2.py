M = int(input())
N = int(input())

prime_list = []

def prime(k):
    if(k == 1):
        return False
    for i in range(2,k):
        if(k % i ==0):
            return False
    return True

for i in range(M, N+1):
    if (prime(i) == True):
        prime_list.append(i)

if(len(prime_list)==0):
    print("-1")
else:
    print(sum(prime_list))
    print(min(prime_list))