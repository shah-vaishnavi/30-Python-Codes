# Tuple operations

roll_numbers = (101, 102, 103, 104, 105)

print("Tuple:", roll_numbers)

print("Indexing:", roll_numbers[0])
print("Slicing:", roll_numbers[1:4])

new_tuple = roll_numbers + (106, 107)

print("Concatenation:", new_tuple)

# Set operations

course1 = {101, 102, 103, 104}
course2 = {103, 104, 105, 106}

print("\nCourse 1:", course1)
print("Course 2:", course2)

print("Union:", course1.union(course2))

print("Intersection:", course1.intersection(course2))

print("Difference:", course1.difference(course2))

print("Symmetric Difference:",
      course1.symmetric_difference(course2))

print("Subset:", course1.issubset(course2))

print("Superset:", course1.issuperset(course2))

course1.add(107)
print("After Adding:", course1)

course1.discard(101)
print("After Removing:", course1)

squares = {x * x for x in range(1, 11) if x % 2 == 0}

print("Squares of Even Numbers:", squares)