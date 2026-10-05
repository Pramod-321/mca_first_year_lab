array=[2,5,8,9,1]
print(array)
n=len(array)
print(n)
smallest=array[0]
largest=array[0]
for i in range ( 1 , n):
    if array[i] < smallest :
        smallest = array[i]
    if array[i] > largest :
       largest = array[i]
print(smallest)
print(largest)       

