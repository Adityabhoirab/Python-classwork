# Program: Print multiplication tables from 5 to 10

for num in range(5, 11):
    print(f"Table of {num}:")
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
    print()  # Adds a blank line after each table for better readability

