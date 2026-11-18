text = input("Enter a sentence: ")

print("Length:", len(text))

print("Uppercase:", text.upper())

print("Lowercase:", text.lower())

print("Without spaces:", text.strip())

old = input("Enter word to replace: ")
new = input("Enter new word: ")

print("Replaced String:", text.replace(old, new))

ch = input("Enter character to count: ")

print("Occurrences:", text.count(ch))

start = input("Enter starting substring: ")
end = input("Enter ending substring: ")

print("Starts with:", text.startswith(start))
print("Ends with:", text.endswith(end))

s1 = "Hello"
s2 = "Python"

print("Concatenation:", s1 + " " + s2)

print("Repetition:", s1 * 3)

print("'Python' in sentence:", "Python" in text)