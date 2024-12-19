# Program: Input a list of elements and display them

# Create an empty list
l = []

# Take input from the user for the number of elements
n = int(input("How many elements do you want to enter: "))

# Loop to accept list items from the user
for i in range(0, n):
    l.append(input("Enter the item: "))

# Display the elements in the list
print("The elements in the list are:")
for item in l:
    print(item)
