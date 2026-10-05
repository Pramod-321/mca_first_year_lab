### write an algorithm to find given matrix is sparse or not###

arr=[[0, 0, 3], [0,3,0], [0, 2, 0]] 
zero=0
non_zero=0
for row in arr:
    for element in row:
        if element==0:
            zero+=1
        else:
            non_zero+=1

if zero > non_zero:
    print("The given matrix is sparse" , arr)
else:
    print("The given matrix is not sparse" , arr)

