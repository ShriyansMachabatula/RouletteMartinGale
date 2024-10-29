from flask import Flask, jsonify, request, session
from flask_cors import CORS
import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file, if running locally
load_dotenv()

# Initialize Flask app and set secret keys
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")
# Store your AUTH_KEY here, do not expose it to the client
auth_key = os.getenv("AUTH_KEY")

# Game state variables
balance = 10000
bet = 1.5

# Roulette board setup
board = {
    0: "green",
    1: "red", 2: "black", 3: "red", 4: "black", 5: "red", 6: "black",
    7: "red", 8: "black", 9: "red", 10: "black", 11: "black", 12: "red",
    13: "black", 14: "red", 15: "black", 16: "red", 17: "black", 18: "red",
    19: "red", 20: "black", 21: "red", 22: "black", 23: "red", 24: "black",
    25: "red", 26: "black", 27: "red", 28: "black", 29: "black", 30: "red",
    31: "black", 32: "red", 33: "black", 34: "red", 35: "black", 36: "red"
}

# Route to simulate a single spin


@app.route("/spin/<bet>/<colorChoice>")
def spin_once(bet, colorChoice):
    global balance
    bet = float(bet)  # Ensure bet is handled as a float

    # Randomly select a number and its color from the board
    number, color = random.choice(list(board.items()))

    # Determine if the user won or lost based on color choice
    if colorChoice == color:  # Win condition
        balance += bet * 2
        bet = 1.5  # Reset bet to the base amount on win
    else:  # Loss condition
        balance -= bet
        bet *= 2.5  # Increase the bet amount on loss

    # Store bet in session for persistence
    session['bet'] = bet

    # Return the result as JSON
    return jsonify({
        "result": f"The color is {color}, the number is {number}",
        "balance": balance,
        "next_bet": bet
    })

# Route to reset game state


@app.route("/stop")
def stop():
    global balance, bet
    balance = 10000
    bet = 1.5
    session['bet'] = bet
    return "Game stopped: Balance reset to 10000"


if __name__ == "__main__":
    app.run(debug=True)
