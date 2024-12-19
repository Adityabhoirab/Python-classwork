# Customer ID and Name dictionary
customers = {
    101: 'John Doe',
    102: 'Jane Smith',
    103: 'Tom Brown',
    104: 'Emily White'
}

# Display initial customer list
print("\nCustomer IDs and Names:")
print(customers)

# Operations on customer dictionary
customers[105] = 'Michael Green'  # Add new customer
customers[103] = 'Thomas Brown'  # Update customer information
del customers[102]  # Remove customer
print("\nUpdated customer list:", customers)

