n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = float(input("Enter marks of student " + str(i + 1) + ": "))
    marks.append(mark)

average = sum(marks) / n
highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0
above_75 = 0

for mark in marks:

    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if mark > 75:
        above_75 = above_75 + 1

print("Class Average:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Passed Students:", passed)
print("Failed Students:", failed)
print("Students scoring above 75%:", above_75)