### write a python program to add two matrices take input from user "and display the result"###

n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
print("Enter the elements of first matrix:")    
matrix1 = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)
print("the first matrix is: " ,matrix1)

print("Enter the elements of second matrix:")
matrix2 = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)

print("the second matrix is : " ,matrix2)

# Add the matrices
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)


# Display the result
print("The sum of the two matrices is:")
for row in result:
    print(row)