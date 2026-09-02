matrix = [[],[],[],[],[]]
for i in range(5):
    row = list(map(int,input().rstrip().split()))
    matrix[i]=row
position1=[]
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            position1=[i, j]
middle_x=2
middle_y=2
loc=(abs(position1[0]-middle_x)
     +abs(position1[1]-middle_y)) #abs returns absolute value of a number
                                #i.e,it removes the sign and gives the distance from zero.
print(loc)
