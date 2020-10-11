T = int(input())
for i in range(T):
    N = int(input())

    zero = 0
    one = 0

    def fibo(n):
        global zero
        global one
        if (n == 0):
            zero+=1
            return 0
        elif (n == 1):
            one +=1
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)

    fibo(N)
    print(zero, one)
