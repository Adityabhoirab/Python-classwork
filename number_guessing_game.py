import random

# Start the game
for i in range(1, 4):
    # Accept input from the user
    num1 = int(input("Enter a number between 1 and 10: "))
    
    # Generate a random number between 1 and 10
    tem = random.randint(1, 10)
    
    # Display the entered and generated number
    print(f"You entered the number {num1} and the random number is {tem}")
    
    # Check if the user wins or loses
    if num1 == tem:
        print("You win!")
        break  # Exit the loop if the user wins
    else:
        print("You lose the game")
