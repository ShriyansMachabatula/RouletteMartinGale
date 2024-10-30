from flask import Flask, session, jsonify
from flask_cors import CORS
import random
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv("SECRET_KEY")  # Fetch the secret key

app = Flask(__name__)
CORS(app)
app.secret_key = SECRET_KEY

balance = 10000
stop_flag = False
bet = 1.5

board = {
    0: "green",
    1: "red", 2: "black", 3: "red", 4: "black", 5: "red", 6: "black",
    7: "red", 8: "black", 9: "red", 10: "black", 11: "black", 12: "red",
    13: "black", 14: "red", 15: "black", 16: "red", 17: "black", 18: "red",
    19: "red", 20: "black", 21: "red", 22: "black", 23: "red", 24: "black",
    25: "çred", 26: "black", 27: "red", 28: "black", 29: "black", 30: "red",
    31: "black", 32: "red", 33: "black", 34: "red", 35: "black", 36: "red"
}


@app.route("/spin/<bet>/<colorChoice>")
def spin_once(bet, colorChoice):
    global balance
    number, color = random.choice(list(board.items()))

    bet = float(bet)  # Ensure bet is a float

    if colorChoice == color:  # Player wins
        balance += bet * 2
        bet = bet  # Reset bet to 1.5 on win
    else:  # Player loses
        balance -= bet
        bet = bet * 2.5  # Increase the bet on loss

    session['bet'] = bet  # Store the updated bet in session

    return jsonify(f"The color is {color}, the number is {number}, the balance is {balance}, and the next bet is {bet}")


@app.route("/stop")
def stop():
    balance = 10000
    session['bet'] = 1.5
    return "Game stopped: Balance reset to 10000"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))




    
