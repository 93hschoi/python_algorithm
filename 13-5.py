N = int(input())
num = 0

for i in range(100, 100000):
    string = str(i)

    if('666' in string):
        num+=1
        if(num ==N):
            print(i)
