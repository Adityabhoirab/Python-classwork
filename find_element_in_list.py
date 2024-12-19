# Program to search for an element in a list

l = [89, 76, 34, 23, 11]  # List of elements
ele = 34  # Element to search for

# Loop through the list to check if the element exists
for i in l:
    if i == ele:
        print(f"{ele} is in the list.")
        break
else:
    print(f"{ele} is not in the list.")  # If the loop completes without finding the element
