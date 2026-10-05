""" i = 10
even=[]
odd=[]
while i >= 0:
    if i % 2 == 0 :
        even.append(i)
    else :
        odd.append(i)
    i=i-1
print("Even number :",even)
print("odd number : ",odd) """


i = 10

print("Even numbers:", end=" ")
while i >= 0:
    if i % 2 == 0:
        print(i, end=" ")
    i -= 1

i = 10
print("\nOdd numbers:", end=" ")
while i >= 0:
    if i % 2 != 0:
        print(i, end=" ")
    i -= 1

