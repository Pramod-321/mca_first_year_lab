numbers = [4, 8, 12, 16, 20]
search_number = int(input("Enter a number to search: "))
found = False

for number in numbers:
    if number == search_number:
        print("Number found")
        found = True
        break

if found == False:
    print("Number not found")
