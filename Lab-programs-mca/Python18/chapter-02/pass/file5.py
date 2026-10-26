# pass represents a branch that will be completed later.
choice = input("Enter yes or no: ")

if choice == "yes":
    print("You selected yes")
elif choice == "no":
    pass
else:
    print("Please enter yes or no")

print("Program finished")
