# Program: Sum of even numbers between 1 and 20 using a while loop

n = 2  # Start from the first even number
sum1 = 0  # Initialize sum

while n <= 20:
    sum1 = sum1 + n  # Add the current even number to the sum
    n += 2  # Increment by 2 to get the next even number

print("The sum of even numbers between 1 and 20 is:", sum1)
