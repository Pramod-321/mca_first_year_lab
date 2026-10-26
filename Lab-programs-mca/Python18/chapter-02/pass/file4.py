# pass does nothing and can be used as a placeholder.
number = 1

while number <= 5:
    if number == 3:
        pass
    else:
        print(number)
    number = number + 1

print("While loop finished")
