number = int(input("Enter a non-negative number: "))
factorial = 1

for value in range(1, number + 1):
    factorial = factorial * value

print("Factorial:", factorial)
