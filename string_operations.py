# String related methods

strmsg = "helloworld!!"

# Converting data to lowercase
new_msg = strmsg.lower()
print("The lowercase string is:", new_msg)

# Converting data to uppercase
upp_msg = strmsg.upper()
print("The uppercase string is:", upp_msg)

# Removing spaces from the beginning and at the end
name = "      sangeeta "
final_name = name.strip()
print("The stripped string (both sides):", final_name)

# Removing left space
lspace = name.lstrip()
print("The left space removed:", lspace)

# Removing right space
rspace = name.rstrip()
print("The right space removed:", rspace)

# str.replace(old, new): This method replaces all occurrences of the "old" substring 
# with the "new" substring in the string
sentence = "i like apples, and i like pineapple."
new_sentence = sentence.replace("like", "love")
print("After replace operation:", new_sentence)
