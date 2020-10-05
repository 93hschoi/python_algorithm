def prime(k):
    if(k ==1):
        return False
    for i in range(2,k):
        if(k % i ==0):
            return False
    return True

while(True):
    N = int(input())
    list_prime = []
    for i in range(N+1,2*N+1):
        if(prime(i)==True):
            list_prime.append(i)
    print(len(list_prime))

#timeless