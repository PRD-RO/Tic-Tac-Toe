This project contains two separate Tic-Tac-Toe implementations written in Python.
One runs in the terminal. The other uses Tkinter to provide a graphical interface with a basic AI opponent.
Both versions support Player vs Player and Player vs Computer modes. 
Features

GUI Version (Tic_Tac_Toe.py)

-Tkinter interface
-Player vs Player
-Player vs Computer
-AI decision logic (Minimax-style evaluation)
-Symbol selection (X or O)
-Control who starts
-Restart button
-Win / tie detection

Console Version (XOGame.py)

-Terminal interface
-Player vs Player / Player vs Computer
-Input validation
0Simple replay loop
-Clean board updates

Requirements
-Python 3.8+
-Tkinter (built-in on most Python installations)
-No external dependencies

Technical Overview

-Both implementations share similar game logic:
-3×3 board stored as a flat array/dictionary
-Win conditions checked across rows, columns, diagonals
-Tie detected when board fills with no winner
-The GUI AI uses a simplified Minimax scoring strategy:
-AI win → +1
-Tie → 0
-Player win → −1
-The AI evaluates available moves and chooses the highest scoring action.

Purpose

This project showcases the difference between terminal-driven
and event-driven game implementations in Python while introducing
basic AI decision making and UI programming.
