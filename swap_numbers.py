# Program: Swap Two Numbers Using a Third Variable

# Take input for the first and second number
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

# Use a third variable to swap the numbers
temp = n1
n1 = n2
n2 = temp

# Display the numbers after swapping
print(f"After swapping: n1 = {n1}, n2 = {n2}")
