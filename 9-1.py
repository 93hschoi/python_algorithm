a, b, c = map(int, input().split())
num = 100

for i in range(num):
    cost = a + (b * i)
    income = c * i
    if (income > cost):
        print(i)
        break

