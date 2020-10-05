S = input()
S = S.lower()    #문자열 전체 소문자로 바꿈
num = [0]*26
Alp = [0]*26

for i in range(0,26):
    Alp[i] = i+97

for i in range(len(Alp)):
    for j in range(len(S)):
        if(Alp[i] == ord(S[j])):
            num[i]+=1

max_number = max(num)
a=0
for i in range(len(num)):
    if(num[i] == max_number):
       a+=1


if(a>1):
    print("?")
else:
    print(chr(num.index(max_number)+65))