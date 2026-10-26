limit = int(input("Enter a limit: "))
number = 1

while number <= limit:
    print(number)
    if number == limit:
        break
    number = number + 1

print("Reached the limit")
