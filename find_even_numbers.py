#wap to find even numbers in the list 
# List of numbers
numbers = [34, 23, 12, 7, 91, 27]

# Empty list to store even numbers
even = []

# Loop through each number in the list
for n in numbers:
    if n % 2 == 0:  # Check if the number is even
        even.append(n)  # Append the even number to the 'even' list

# Print the list of even numbers
print(even)
