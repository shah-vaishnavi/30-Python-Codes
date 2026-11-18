import random

print("Random Integer:", random.randint(1, 100))

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Random Element:", random.choice(fruits))

random.shuffle(fruits)

print("Shuffled List:", fruits)