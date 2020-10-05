a, b = map(int,input().split())
a1=0
a2=0
a3=0

def reverse(k):
    a1 = k//100
    a2 = k//10 - a1*10
    a3 = k%10
    return a3*100 + a2*10 + a1

a = reverse(a)
b = reverse(b)
print(max(a,b))