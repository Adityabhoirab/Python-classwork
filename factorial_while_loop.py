# Program: Find the factorial of a positive number using a while loop

num = int(input("Enter a positive number: "))  # Take input from the user

i = 1  # Initialization
result = 1  # Start with a result of 1

while i <= num:
    result *= i  # Multiply the current result with i
    i += 1  # Increment i

print(f"The factorial of {num} is {result}.")
