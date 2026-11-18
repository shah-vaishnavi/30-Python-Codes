name = input("Enter full name: ")
email = input("Enter email address: ")
mobile = input("Enter mobile number: ")

words = name.split()

first_name = words[0]
last_name = words[-1]

print("\nFirst Name:", first_name)
print("Last Name:", last_name)

print("Reversed Name:", name[::-1])

username, domain = email.split("@")

print("Email Username:", username)
print("Email Domain:", domain)

print("Last Four Mobile Digits:", mobile[-4:])

print("\nStudent Information")

print(f"Name: {name}")
print("Email: {}".format(email))
print("Mobile Number: %s" % mobile)

print("\nPositive Indexing:", name[0])
print("Negative Indexing:", name[-1])