# Program: Age Eligibility for Different Classes

# Take input for the child's age
age = int(input("Enter the child's age: "))

# Check eligibility using if...elif...else
if age < 3:
    print("Eligible for play group.")
elif 3 <= age < 4:
    print("Eligible for Nursery.")
elif 4 <= age < 5:
    print("Eligible for Jr. KG.")
elif 5 <= age < 6:
    print("Eligible for Sr. KG.")
else:
    print("Not eligible for any of these classes.")
