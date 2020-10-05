N = int(input())
a = 1
b = 1
num = 0  #분자
den = 0  #분모

def sum(k):
    s = 0
    for i in range(1,k+1):
        s += i
    return s

for i in range(100):
    a += i
    b = a + i
    if(a<=N<=b):
        # i+1 번째
        # 분자+분모 = i+2
        if(i%2 ==0):
            den = 0
            den = N - sum(i)
            num = (i+2) - den
        else:
            num = 0
            num = N - sum(i)
            den = (i+2) - num

print(num,"/",den)
