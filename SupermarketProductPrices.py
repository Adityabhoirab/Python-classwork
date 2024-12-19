# Supermarket product prices dictionary
supermarket = {
    'apple': 1.5,
    'banana': 0.8,
    'carrot': 1.0,
    'milk': 2.5,
    'bread': 1.2
}

# Display initial supermarket product prices
print("Supermarket products and prices:")
print(supermarket)

# Operations on supermarket dictionary
print("\nPrice of apple:", supermarket['apple'])
supermarket['orange'] = 1.8  # Add new product
supermarket['banana'] = 0.75  # Update existing product
del supermarket['bread']  # Remove product
print("\nUpdated supermarket list:", supermarket)
