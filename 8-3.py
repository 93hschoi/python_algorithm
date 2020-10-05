S = input()
check_list = [-1]*26

for i in range(97,123):
    for j in range(len(S)):
        if( i == ord(S[j])):
            check_list[i-97] = j

print(check_list)

