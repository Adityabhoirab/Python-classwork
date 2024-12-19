# Program: Print all even numbers between 1 and 20 using a for loop

print("Even numbers between 1 and 20:")
for n in range(1, 21):  # Loop through numbers from 1 to 20
    if n % 2 == 0:  # Check if the number is even
        print(n)
