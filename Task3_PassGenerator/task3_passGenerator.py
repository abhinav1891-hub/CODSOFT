# Random Password Generator
# Developed for CodSoft Internship

import random

print("===== Password Generator =====")

# User input
length = int(input("Enter password length: "))

# Manually define characters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Output
print("\nGenerated Password:", password)