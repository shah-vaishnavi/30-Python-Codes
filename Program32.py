def student_result(name, *args, **kwargs):
    total = sum(args)
    average = total / len(args)
    highest = max(args)

    print("\nStudent Name:", name)
    print("Roll Number:", kwargs.get("roll_no"))
    print("Class:", kwargs.get("class_name"))

    return total, average, highest

name = input("Enter student name: ")

marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total, average, highest = student_result(
    name, *marks, roll_no=101, class_name="MCA"
)

print("\nTotal Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)