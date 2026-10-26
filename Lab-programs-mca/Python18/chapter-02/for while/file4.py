last_number = int(input("Enter a positive number: "))
total = 0
number = 1

while number <= last_number:
    total = total + number
    number = number + 1

print("Sum of natural numbers:", total)
