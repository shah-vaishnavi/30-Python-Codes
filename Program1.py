Students_marks = []
for i in range(5):
    marks = int(input("Enter 5 subject marks:"))
    Students_marks.append(marks)
    print("Marks:",marks)
    total_marks = sum(Students_marks)
    average = total_marks/5
    percentage = (total_marks/500)*100
print("Total Marks:",total_marks)
print("Average Marks:",average)
print("Percentage:",percentage)