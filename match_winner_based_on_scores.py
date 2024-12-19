# Program: Accept scores of two teams and determine the winner using if-elif-else

# Accepting scores of both teams
ind = int(input("Enter the score of India: "))
pak = int(input("Enter the score of Pakistan: "))

# Determine the winner or if it's a tie
if ind < pak:
    print("Pakistan won the match")
elif ind == pak:
    print("Both teams have equal scores")
else:
    print("India won the match")
