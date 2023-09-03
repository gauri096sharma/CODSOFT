#PASSWORD GENERATOR
import random
import string
import secrets

def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == '4':
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        return "Invalid complexity choice"

    secure_generator = secrets.SystemRandom()
    password = ''.join(secure_generator.choice(characters) for _ in range(length))
    return password

print("Password Generator")
print("Complexity Levels:")
print("1. Letters (lowercase and uppercase)")
print("2. Letters and Digits")
print("3. Letters, Digits, and Special Characters")
print("4. Letters, Digits, Special Characters, and Whitespace")

while True:
    try:
        length = int(input("Enter desired password length: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

complexity = input("Enter complexity level (1/2/3/4): ")

password = generate_password(length, complexity)
print("Generated Password:", password)
