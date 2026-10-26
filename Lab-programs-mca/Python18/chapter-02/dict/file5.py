student = {}
student["name"] = input("Enter student name: ")
student["roll_number"] = input("Enter roll number: ")
student["course"] = input("Enter course: ")

print("Student record")
for key, value in student.items():
    print(key, ":", value)
