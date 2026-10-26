first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter +, -, * or /: ")

if operator == "+":
    print("Answer:", first_number + second_number)
elif operator == "-":
    print("Answer:", first_number - second_number)
elif operator == "*":
    print("Answer:", first_number * second_number)
elif operator == "/" and second_number != 0:
    print("Answer:", first_number / second_number)
elif operator == "/":
    print("Cannot divide by zero")
else:
    print("Invalid operator")
