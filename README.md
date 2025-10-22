🐷 Pig Game

A terminal-based version of the classic Pig dice game, built in Python using an object-oriented approach.
The game can be played in single-player mode (against the computer) or two-player mode.

🎮 Game Description

Pig is a simple dice game where players take turns rolling a die to accumulate points.
Each player’s turn continues until they either:

Roll a 1 – losing all points gained that turn, or
Hold – adding their turn score to their total score.
The first player to reach 100 points wins.

The game includes:

Single-player mode (player vs computer)
Two-player mode
Configurable player names
A simple computer intelligence system
Persistent high score storage
Option to view game rules

Text-based interface in the terminal

⚙️ Installation
1. Clone the repository
git clone https://github.com/kytkov/a02.git
cd pig-game

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Running the Game

Once installed, start the game from the terminal:
python3 main.py


You will be greeted with a command-line menu where you can:

Start a new game
Choose single-player or two-player mode
View the rules
Check the high scores
Quit or restart the game

🧠 Computer Intelligence

In single-player mode, the computer plays using a basic risk-based strategy:
It keeps rolling until it reaches a certain point threshold per turn.

The difficulty can be adjusted to make the computer play more cautiously or aggressively.

💾 High Scores

The game saves player statistics (such as wins, losses, and total games played) in a persistent storage file.
These scores remain even after restarting the program.

🪄 Features Summary

🎲 Play against another player or the computer

💾 Persistent high score tracking

🧠 Computer intelligence with adjustable difficulty

🧍 Change player names anytime

📜 Display game rules

🧩 Cheat option for faster testing

🚫 Handles invalid input gracefully



🧾 License

This project is open source and available under the MIT License.
See LICENSE.md for details.