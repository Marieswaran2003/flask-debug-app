# app.py
import debugpy
import random
from flask import Flask, jsonify

# Enable debugpy debugger to listen on 0.0.0.0:5678
debugpy.listen(("0.0.0.0", 5678))
print("Waiting for debugger to attach...")
debugpy.wait_for_client()

app = Flask(__name__)

# Quotes list
quotes = [
    "Believe you can and you're halfway there.",
    "Do one thing every day that scares you.",
    "Your limitation—it’s only your imagination.",
    "Sometimes later becomes never. Do it now.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it."
]

@app.route("/")
def home():
    quote = quotes[random.randit(0, len(quotes))] #off-by-one bug
    return jsonify( quote=quote, author="Flask Debugger App")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


#quote = random.choice(quotes)
