students = {"Asha", "Ravi", "Neha", "Kiran"}
name = input("Enter a student name: ")

if name in students:
    print(name, "is present in the set")
else:
    print(name, "is not present in the set")
