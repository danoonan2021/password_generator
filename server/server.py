from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# Validate input
def validate_pwgen(words, nums, caps, symbols):
    try:
        words, nums, caps, symbols = int(words), int(nums), int(caps), int(symbols)
        if any(x < 0 for x in (words, nums, caps, symbols)) or words < max(nums, caps, symbols):
            return False
        return True
    except ValueError:
        return False

# Password generation
def pwgen(words, caps, nums, symbols):
    result = []
    with open("words.txt", "r") as f:
        words_list = [line.strip().lower() for line in f]

    rand = random.choices(words_list, k=words)
    rand.append("")

    while caps > 0:
        word = random.choice(rand)
        if word.islower():
            rand.remove(word)
            rand.append(word.capitalize())
            caps -= 1

    while nums > 0:
        word = random.choice(rand)
        rand.remove(word)
        rand.append(word + random.choice(string.digits))
        nums -= 1

    while symbols > 0:
        word = random.choice(rand)
        rand.remove(word)
        rand.append(word + random.choice(string.punctuation))
        symbols -= 1

    random.shuffle(rand)
    return "".join(rand)

@app.route("/generate", methods=["POST"])
def generate_password():
    data = request.json
    words = data.get("words")
    nums = data.get("nums")
    caps = data.get("caps")
    symbols = data.get("symbols")

    if not validate_pwgen(words, nums, caps, symbols):
        return jsonify({"error": "Invalid input"}), 400

    password = pwgen(int(words), int(caps), int(nums), int(symbols))
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
