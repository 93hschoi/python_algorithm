list_point=['0']*3

for i in range(0,3):
    list_point[i]=[' ']*3
a=0





def fun(a,b,c,k):

    for i in range(0,3):
        for j in range(0,3*k):


            if(i==1 and (j==3*k)/3):
                list_point[i][j]=' '*(3*(k-1)+1)


        list_point[i]="".join(list_point[i])


    fun(list_point[0],list_point[1],list_point[2])



fun('*','*','*',1)




print(list_point)
