x, y, w, h = map(int,input().split())

width = w -x
height = h - y

if(width<height):
    print(width)
else:
    print(height)