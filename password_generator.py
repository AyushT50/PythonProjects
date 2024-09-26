import random
import string

"""
Password Generator

This script generates a secure, random password using a combination of uppercase 
and lowercase letters, digits, and punctuation characters. The password length 
can be customized.
"""

# Length of the password
PASSWORD_LENGTH = 12

# Define the character set (uppercase, lowercase, digits, punctuation)
char_values = string.ascii_letters + string.digits + string.punctuation

# Generate the password using list comprehension
password = "".join(random.choice(char_values) for _ in range(PASSWORD_LENGTH))

# Display the generated password
print("Your generated password is:", password)
