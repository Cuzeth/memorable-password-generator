import random

# File names
thirteen_letter_file = 'thirteen_letter_chunks.txt'
eight_letter_file = 'eight_letter_chunks.txt'

# Read the files
with open(thirteen_letter_file, 'r') as file:
    thirteen_letter_chunks = file.read().splitlines()

with open(eight_letter_file, 'r') as file:
    eight_letter_chunks = file.read().splitlines()

# Characters to be appended
special_characters = '!?$&*'

# Generate the random parts
thirteen_letter_word = random.choice(thirteen_letter_chunks)
random_six_digit_number = random.randint(100000, 999999)
special_character = random.choice(special_characters)
eight_letter_word = random.choice(eight_letter_chunks).capitalize()

# Combine the parts
result = f"{thirteen_letter_word}{random_six_digit_number}{special_character}{eight_letter_word}"

# Print the result
print(result)