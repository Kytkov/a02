[![API Docs](https://img.shields.io/badge/API%20Docs-GitHub%20Pages-blue)](https://kytkov.github.io/a02/)

# Pig Dice Game

## Overview
This project is a **terminal-based implementation of the classic Pig Dice Game**, built using **object-oriented programming principles** in Python.  
The game supports both **single-player (against the computer)** and **two-player** modes and includes features such as persistent high scores, configurable player names, and basic computer intelligence.

---

## Game Rules
Pig is a simple dice game where players take turns rolling a die to accumulate points:

- Each player may roll the die as many times as they wish during their turn.  
- If a **1** is rolled, the player loses all points gained during that turn, and control passes to the next player.  
- A player may choose to **hold**, adding the accumulated turn points to their total score.  
- The first player to reach **100 points** wins the game.

---

## Features
- Single-player mode (player vs. computer)  
- Two-player mode  
- Configurable player names  
- Persistent high score tracking  
- Computer opponent with adjustable difficulty (risk-based decision-making)  
- Menu-driven terminal interface  
- Comprehensive unit tests  
- Graceful handling of invalid input  

---

## Requirements
- Python 3.10 or newer  
- Compatible with macOS, Linux, and Windows  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kytkov/a02.git
   cd a02
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Quick Start
Run the game directly from the command line:
```bash
py main.py (dir a02/Pigdicegame)
```
or
```bash
py Pigdicegame/main.py
```

You will be presented with a text-based menu that allows you to:
- Start a new game  
- Choose between single-player or two-player mode  
- View rules  
- Check high scores  
- Quit or restart the game  

---

## Computer Intelligence
In single-player mode, the computer uses a **risk-based strategy** to decide when to stop rolling.  
It continues rolling until it reaches a threshold of turn points, simulating either a cautious or aggressive playstyle.  
This threshold can be adjusted in `Pigdicegame/Intelligence.py`.

---

## High Scores and Statistics
The game stores player statistics — including wins, losses, and total games played — in persistent storage.  
These records remain available even after restarting the program.  
Implementation is handled in `Highscore.py` and `Statistics.py`.

---

## Project Structure
```
Pigdicegame/
 ├── Game.py             # Core game logic and flow control
 ├── dice.py             # Single die implementation
 ├── dicehand.py         # Dice collection and turn logic
 ├── player.py           # Player data model and behavior
 ├── Intelligence.py     # Computer opponent logic
 ├── Highscore.py        # Persistent high score management
 ├── Statistics.py       # Player and game statistics
 ├── main.py             # Entry point (menu and setup)
 ├── __main__.py         # Enables execution via `python -m Pigdicegame`
 ├── Test*.py            # Unit tests for modules
```

---

## Development

A `Makefile` is included to simplify development tasks.

| Command         | Description                                                   |
|-----------------|---------------------------------------------------------------|
| `make install`  | Install development dependencies                              |
| `make run`      | Run the game (`RUN_MODULE` defaults to `Pigdicegame.main`)    |
| `make test`     | Run all unit tests                                            |
| `make coverage` | Generate a test coverage report in `doc/coverage`             |
| `make lint`     | Run static analysis with Flake8 and Pylint                    |
| `make format`   | Format code using Black                                       |
| `make doc`      | Generate API documentation using `pdoc` (output to `doc/api`) |

---

## Testing
Run all unit tests:
```bash
python3 -m unittest discover Pigdicegame
```
or use:
```bash
make test
```

---

## Documentation
To generate local documentation (if `pdoc` is installed):
```bash
make doc
```
Documentation files are generated in the `doc/api` directory.

---

## Troubleshooting
- If imports fail on case-sensitive systems (e.g., Linux), ensure the project is executed as a **module**:
  ```bash
  python3 -m Pigdicegame
  ```
- When adding new modules, use **relative imports** (e.g., `from .Game import Game`) to maintain package consistency.

---

## License
This project is open source and available under the **MIT License**.  
See [LICENSE.md](LICENSE.md) for full license information.
