from flask import Flask, jsonify, send_from_directory, session
from flask_cors import CORS
import random
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")

# Game state variables
balance = 10000
bet = 1.5
board = {
    0: "green",
    1: "red", 2: "black", 3: "red", 4: "black", 5: "red", 6: "black",
    7: "red", 8: "black", 9: "red", 10: "black", 11: "black", 12: "red",
    13: "black", 14: "red", 15: "black", 16: "red", 17: "black", 18: "red",
    19: "red", 20: "black", 21: "red", 22: "black", 23: "red", 24: "black",
    25: "red", 26: "black", 27: "red", 28: "black", 29: "black", 30: "red",
    31: "black", 32: "red", 33: "black", 34: "red", 35: "black", 36: "red"
}

# Serve index.html at the root


@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

# Serve static files (like CSS and JS)


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory(".", filename)

# API endpoint to handle the game spin


@app.route("/spin/<bet>/<colorChoice>")
def spin_once(bet, colorChoice):
    global balance
    number, color = random.choice(list(board.items()))

    bet = float(bet)  # Convert bet to float

    if colorChoice == color:  # Win condition
        balance += bet * 2
    else:  # Loss condition
        balance -= bet
        bet *= 2.5  # Increase the bet on loss

    session['bet'] = bet  # Store updated bet in session

    return jsonify(f"The color is {color}, the number is {number}, the balance is {balance}, and the next bet is {bet}")

# API endpoint to reset the game


@app.route("/stop")
def stop():
    global balance
    balance = 10000
    session['bet'] = 1.5
    return "Game stopped: Balance reset to 10000"


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
