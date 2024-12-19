# Program 1: Print numbers from 1 to 50
print("Printing numbers from 1 to 50:")
for i in range(1, 51):
    print(i)

# Program 2: Accept a number from the user and print its multiplication table
num = int(input("Enter the number to print its table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Program 3: Nested Loop Example (not sure about your intent, here's a generic example)
print("Printing numbers in a nested loop:")
for i in range(2, 7):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
