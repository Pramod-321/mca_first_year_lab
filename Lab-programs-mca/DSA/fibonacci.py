arr=[1,2,3,4,5]
a=0
b=1
n=len(arr)
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
print(c)