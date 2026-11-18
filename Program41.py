# Write student details

file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")

file.write("Student Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")

file.close()

# Read complete file

file = open("student.txt", "r")

print("\nFile Contents:")
print(file.read())

file.close()

# Append additional records

file = open("student.txt", "a")

name = input("\nEnter another student name: ")
roll = input("Enter roll number: ")

file.write("\nStudent Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")

file.close()

# Read file line by line

file = open("student.txt", "r")

print("\nUpdated File Contents:")

for line in file:
    print(line, end="")

file.close()

print("\n\nFile closed successfully")