n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Original List:", numbers)

pos = int(input("Enter position to insert: "))
value = int(input("Enter value to insert: "))

numbers.insert(pos, value)

print("After Insertion:", numbers)

remove_value = int(input("Enter element to remove: "))

if remove_value in numbers:
    numbers.remove(remove_value)

print("After Removal:", numbers)

print("Ascending Order:", sorted(numbers))
print("Descending Order:", sorted(numbers, reverse=True))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

print("Concatenation:", numbers + [100, 200])
print("Repetition:", numbers * 2)

print("First Element:", numbers[0])

search = int(input("Enter element to search: "))
print("Membership:", search in numbers)

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
squares = [x ** 2 for x in numbers]

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Squares:", squares)

numbers.append(50)
numbers.extend([60, 70])
numbers.reverse()

print("Final List:", numbers)