def hino(count,start,to,temp):
    if(count<1):
        return
    hino(count-1,start,temp,to)
    print(count,"원반을",start,"에서",to,"로 옮김")
    hino(count-1,temp,to,start)

hino(3,1,3,2)