#wap to get average of three numbers using class and object



class Average:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_average(self):
        return (self.num1 + self.num2 + self.num3) / 3

# User input
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

# Create object of Average class
avg = Average(n1, n2, n3)

# Output result
print("The average is:", avg.calculate_average())
