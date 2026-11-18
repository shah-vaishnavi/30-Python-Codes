employees = {
    101: {
        "name": "Amit",
        "department": "IT",
        "salary": 50000
    },
    102: {
        "name": "Rahul",
        "department": "HR",
        "salary": 40000
    },
    103: {
        "name": "Priya",
        "department": "Finance",
        "salary": 60000
    }
}

print("Employee Details:")

print(employees)

# Add employee

employees[104] = {
    "name": "Neha",
    "department": "IT",
    "salary": 55000
}

# Update employee

employees[101]["salary"] = 65000

# Display keys and values

print("\nKeys:", employees.keys())

print("Values:", employees.values())

print("Items:", employees.items())

# Search employee

emp_id = int(input("\nEnter Employee ID: "))

if emp_id in employees:
    print("Employee Found:", employees[emp_id])
else:
    print("Employee Not Found")

# Dictionary comprehension

salary_limit = int(input("\nEnter minimum salary: "))

high_salary = {
    emp_id: details
    for emp_id, details in employees.items()
    if details["salary"] > salary_limit
}

print("\nEmployees earning above specified salary:")
print(high_salary)

# Delete employee

del employees[102]

print("\nFinal Employee Records:")
print(employees)