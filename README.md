 Tic-Tac-Toe Game Suite (GUI & CLI)

This repository contains two separate implementations of the classic **Tic-Tac-Toe** game written in Python. It demonstrates the structural and conceptual differences between terminal-driven (CLI) and event-driven (GUI) applications, while incorporating basic AI decision-making.

---

Features

###  GUI Version (`Tic_Tac_Toe.py`)
- **Tkinter Interface:** Clean graphical user interface.
- **Game Modes:** Player vs Player & Player vs Computer.
- **AI Opponent:** Powered by Minimax-style decision logic.
- **Customization:** Symbol selection (X or O) and control over who plays first.
- **Controls & Detection:** Interactive restart button and instant win/tie detection.

###  Console Version (`XOGame.py`)
- **Terminal Interface:** Lightweight command-line interface.
- **Game Modes:** Player vs Player & Player vs Computer.
- **Robust Input:** Built-in input validation to prevent invalid moves.
- **Replay Loop:** Simple option to start a new game immediately.

---

##  Technical Overview

Both implementations share core game rules and logic:
- **Board Representation:** 3×3 grid managed via array/dictionary structures.
- **Win/Tie Conditions:** Continuous evaluation across rows, columns, and diagonals.
- **Minimax AI Logic:** The GUI's AI evaluates potential moves using a simplified scoring system:
  - **AI Win:** `+1`
  - **Tie:** `0`
  - **Player Win:** `-1`
  
The AI recursively evaluates available moves to select the path with the highest outcome score.

---

##  Requirements & Installation

- **Python 3.8+**
- **Tkinter** (Pre-installed with standard Python distributions)
- **No external dependencies** required.

### How to Run

1. **Run the Graphical Version (GUI):**
   ```bash
   python Tic_Tac_Toe.py
   
Run the Command Line Version (CLI):
Bash
   python XOGame.py


Purpose
This project showcases fundamental software engineering concepts in Python, contrasting standard procedural/terminal loops with event-driven GUI architecture, along with basic algorithmic decision-making.
