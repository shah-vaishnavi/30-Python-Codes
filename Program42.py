try:
    file = open("student.txt", "r")

    print("File Name:", file.name)
    print("File Mode:", file.mode)

    print("\nUsing read():")
    print(file.read())

    print("Current Position:", file.tell())

    file.seek(0)

    print("\nUsing readline():")
    print(file.readline())

    file.seek(0)

    print("\nUsing readlines():")
    print(file.readlines())

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

else:
    print("File operations completed successfully")

finally:
    if 'file' in locals() and not file.closed:
        file.close()

    print("File operation completed")