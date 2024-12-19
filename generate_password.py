import random
import string

def generate_password(length=12, use_special_chars=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a pool of characters based on the options
    characters = lowercase + uppercase + digits
    if use_special_chars:
        characters += special_chars

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password(length=16, use_special_chars=True)
print("Generated Password:", password)
