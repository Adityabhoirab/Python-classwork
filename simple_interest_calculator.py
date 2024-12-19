#wap to get simple interest using class and object  

class SimpleInterest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        return (self.principal * self.rate * self.time) / 100

# User input
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

# Create object
si = SimpleInterest(p, r, t)

# Output result
print("Simple Interest:", si.calculate())

