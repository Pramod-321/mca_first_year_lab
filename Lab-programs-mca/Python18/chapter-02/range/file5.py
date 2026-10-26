last_number = int(input("Enter the last number: "))
total = 0

for number in range(1, last_number + 1):
    total = total + number

print("Sum from 1 to", last_number, "is", total)
