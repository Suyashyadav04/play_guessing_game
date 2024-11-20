# Guessing Game

A simple Python-based number guessing game where the computer randomly selects a number, and the user tries to guess it. The game provides feedback to guide the player closer to the correct number.

## Features

- Random number generation using Python's `random` module.
- Customizable range for guessing.
- Feedback on whether the guess is too high, too low, or correct.
- Tracks the number of attempts taken by the user.

## How It Works

1. The program randomly selects a number within a specified range (default: 1 to 100).
2. The user makes a guess.
3. The program provides feedback:
   - "Too high!" if the guess is above the target number.
   - "Too low!" if the guess is below the target number.
   - "Correct!" when the user guesses the number.
4. The game ends when the user guesses the correct number, and the total attempts are displayed.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Game

1. Clone or download the repository.
2. Open a terminal and navigate to the directory containing the script.
3. Run the game:
   ```bash
   python guessing_game.py
