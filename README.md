PYTHON CHESS GAME

Description:
This is a simple chess game that has been developed using the Python programming language and the turtle graphics library. The main objective of this project was to practice python programming skills and maybe learn some concepts of game development along the way.

Features:
Graphical Chessboard – Displays an 8x8 chessboard using turtle graphics
Chess Pieces – The pieces are represented on the board using unicode characters
Pieces Movement – Implements the logic that determines how different pieces move on the board
Turn Management – Alternates between white and black after successful valid moves
Check Detection – Includes logic that determines whether a king is under attack
Checkmate Detection - Includes logic for checking whether a player has been checkmated by confirming if it has any possible escape from a check move

Technologies Used:
- Python3
- Python Turtle Library

Installation:
- Clone this repository or download the project files
    • git clone https://github.com/Allan205/Chess_Game
- Navigate to your cloned repository
- Run this command to start the game:
    • python3 chess_game.py

How to Play:
    • White moves first.
    • Players take turns moving their pieces.
    • Select a piece by clicking on its square.
    • Select another square to attempt to move the selected piece.
    • Only moves accepted by the implemented validation logic are executed.
    • The game includes basic king safety and checkmate detection.

Limitations:
When working on this game, the main objective was to create a simple chess game where basic chess moves can be executed (ie each individual piece moves correctly and the game can detect when a king is in check or checkmate and act accordingly). This core objective has been achieved by the existing code base.
However, there are some other features that were not added due to their added complexity or lack of time (or both…). These features include:
    • Pawn promotion
    • En Passant
    • Castling

NOTE:
The file ‘chess_game.py’ contains the main code for the entire game. The other files contains the isolated implementations of the different features. Example, ‘pawn.py’ contains the isolated implementation of how the pawn moves in the game, ‘checkmate.py’ contains the isolated implementation of check and checkmate features etc...
