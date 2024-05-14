import random
import re
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# File names
common_words_file = '5000-more-common.txt'
thirteen_letter_file = 'thirteen_letter_chunks.txt'
eight_letter_file = 'eight_letter_chunks.txt'

# Read the common words file
with open(common_words_file, 'r') as file:
    common_words = file.read().splitlines()

# Filter common words to get 13-letter and 8-letter words
common_thirteen_letter_words = [word for word in common_words if len(word) == 13]
common_eight_letter_words = [word for word in common_words if len(word) == 8]

# Read the original files
with open(thirteen_letter_file, 'r') as file:
    thirteen_letter_chunks = file.read().splitlines()

with open(eight_letter_file, 'r') as file:
    eight_letter_chunks = file.read().splitlines()

# Characters to be appended
special_characters = '!?$&*'

# Function to calculate word score (lower score is more memorable)
def word_score(word):
    scrabble_scores = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
        'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
        'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    return sum(scrabble_scores[char] for char in word.lower())

# Function to calculate number score (lower score is more memorable)
def number_score(number):
    number_str = str(number)
    if re.search(r'(\d)\1{2,}', number_str):  # Check for repeating digits
        return 1
    elif re.search(r'012|123|234|345|456|567|678|789', number_str):  # Check for sequences
        return 1
    else:
        return 2

# Function to select a random item from the top N items with the lowest scores
def select_top_n(items, score_func, n=1027):
    scored_items = sorted(items, key=score_func)
    return random.choice(scored_items[:n])

# Function to leetify words
def leetify(word, probability=0.3):
    leet_map = {
        'a': '4', 'b': '8', 'e': '3', 'i': '1', 'l': '1',
        'o': '0', 's': '5', 't': '7', 'g': '9'
    }
    return ''.join(leet_map.get(char, char) if random.random() < probability else char for char in word.lower())

@app.route('/generate', methods=['GET'])
def generate_password():
    use_common = request.args.get('use_common', 'false').lower() == 'true'
    leetify_words = request.args.get('leetify', 'false').lower() == 'true'
    leetify_probability = float(request.args.get('leetify_probability', '0.3'))

    if use_common:
        # Use common words
        selected_thirteen_letter_chunks = common_thirteen_letter_words
        selected_eight_letter_chunks = common_eight_letter_words
        # Select a memorable 13-letter word
        thirteen_letter_word = select_top_n(selected_thirteen_letter_chunks, word_score)
        # Select a memorable 8-letter word
        eight_letter_word = select_top_n(selected_eight_letter_chunks, word_score).capitalize()
    else:
        # Use original method without scoring
        thirteen_letter_word = random.choice(thirteen_letter_chunks)
        eight_letter_word = random.choice(eight_letter_chunks).capitalize()

    # Select a memorable 6-digit number
    possible_numbers = [random.randint(100000, 999999) for _ in range(1000)]
    random_six_digit_number = select_top_n(possible_numbers, number_score)

    # Leetify words if toggle is enabled
    if leetify_words:
        thirteen_letter_word = leetify(thirteen_letter_word, leetify_probability)
        eight_letter_word = leetify(eight_letter_word, leetify_probability).capitalize()

    # Select a random special character
    special_character = random.choice(special_characters)

    # Combine the parts
    result = f"{thirteen_letter_word}{random_six_digit_number}{special_character}{eight_letter_word}"

    return jsonify(result=result)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
