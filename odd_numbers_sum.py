# Initialize variables
count = 1        # To keep track of how many odd numbers we've printed
odd_number = 1   # First odd number
sum_of_odds = 0  # To store the sum of the first 100 odd numbers

# While loop to generate and print the first 100 odd numbers
while count <= 100:
    print(odd_number)
    sum_of_odds += odd_number  # Add the odd number to the sum
    odd_number += 2            # Move to the next odd number
    count += 1                 # Increment the counter

# After the loop ends, print the sum of the first 100 odd numbers
print("\nSum of the first 100 odd numbers:", sum_of_odds)
