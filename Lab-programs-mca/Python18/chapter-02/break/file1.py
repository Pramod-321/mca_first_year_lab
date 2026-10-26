stop_number = int(input("Enter a stopping number: "))

for number in range(1, 11):
    if number == stop_number:
        break
    print(number)

print("Loop stopped")
