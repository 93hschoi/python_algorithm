string=[]

lista=[]
n=int(input())
def a(count):
    z="".join(string)
    if(count==n):


        if(len(z)==count):
            lista.append(z)
        return
    if(len(z)!=n):
        for i in range(0,2):
            if(i==0):
                string.append('1')

                a(count+1)
                del string[count]

            else:
                string.append('00')
                a(count+1)
                del string[count]
    else:
        a(count+1)
a(0)
print(lista)


