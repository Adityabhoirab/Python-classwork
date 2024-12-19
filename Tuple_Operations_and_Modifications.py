# WAP to reverse the given tuple
tup1 = (56, 78, 34, 89, 8)
print("The original tuple is:", tup1)
res = tup1[::-1]  # Reverse the tuple
print("The reversed tuple is:")
print(res)

# WAP to print even numbers from the tuple
print("\nEven numbers from the tuple:")
for i in tup1:
    if i % 2 == 0:
        print(i)

# WAP to access elements of a nested tuple
tup2 = (45, [78, 89], 80, 73)
print("\nAccessing elements in nested tuple:")
print(tup2[0])  # First element
print(tup2[1])  # Second element
print(tup2[1][0])  # First element of the list in the tuple
print(tup2[1][1])  # Second element of the list in the tuple

# Modifying a list inside a tuple
tup2[1][0] = 45  # Changing the first element of the list inside the tuple
print("\nAfter modifying the list inside the tuple:")
print(tup2)

# Tuple cannot be changed (immutable)
# Uncommenting the next line will raise a TypeError because tuples are immutable
# tup2[2] = 78  # This will raise an error

# WAP to count the occurrences of 45 in the tuple
print("\nThe number 45 occurs", tup2.count(45), "times in the tuple.")

# WAP to create a tuple with different data types
my_tuple = ("Maggie", 3, 15.5, True)
print("\nTuple with mixed data types:")
print("I want to eat:", my_tuple)

# Tuple with marks
marks = 23, 67, 87, 34
print("\nI have got marks as:")
print(marks)

# WAP to create a tuple with a single item
price = 34,  # Note the comma here to make it a tuple
print("\nSingle item tuple:")
print(price)
