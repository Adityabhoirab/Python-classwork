# WAP to find addition and subtraction using inheritance concept

# Base class for arithmetic operations (addition and subtraction)
class ArithmeticOperations:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# Derived class that inherits from ArithmeticOperations
class Calculator(ArithmeticOperations):
    pass  # No additional functionality needed, it simply inherits the methods

# Accepting input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Creating an instance of the Calculator class
calc = Calculator()

# Performing addition and subtraction using the inherited methods
addition_result = calc.add(num1, num2)
subtraction_result = calc.subtract(num1, num2)

# Displaying the results
print(f"The sum of {num1} and {num2} is: {addition_result}")
print(f"The difference between {num1} and {num2} is: {subtraction_result}")



