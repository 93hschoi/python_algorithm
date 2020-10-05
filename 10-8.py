while (True):
    length_list = []
    a, b, c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break
    length_list.append(a)
    length_list.append(b)
    length_list.append(c)
    length_list.sort()

    A = length_list[0]
    B = length_list[1]
    C = length_list[2]

    if (C ** 2 == A ** 2 + B ** 2):
        print("right")
    else:
        print("wrong")




