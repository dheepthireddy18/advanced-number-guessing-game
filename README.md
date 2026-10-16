# advanced-number-guessing-game

 A number guessing game that runs in the terminal. The computer picks a secret number, and the player guesses it with "too low" and "too high" hints. The player chooses a difficulty level and can play in a timed mode. 

 ## Features
 *Feature 1 - Classic Mode:* The computer randomly selects a secret number, and the player guesses it using “too low” and “too high” hints. The game tracks valid attempts, validates input, and displays the result.
 *Feature 2 – Difficulty Levels:* Players choose Easy, Medium, or Hard, each with a different number range and attempt limit.
*Feature 3 – Time Challenge:* Players can choose a 60-second timed mode, where they must guess the secret number before time runs out while staying within the selected difficulty's attempt limit.

## Requirements
- Python 3
- Python editor of your choice

## How to Run
- Clone or download this repository.
- Open the project folder in your terminal
- Create and activate your virtual environment

```python3 -m venv .venv```
```source .venv/bin/activate```

- Run the game
```python3 guess.py```


## Test Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Too-low and too-high guesses | Set the secret number to 45 and entered 37 and 47 | display correct "too low" and "too high" hints | for 50 it showed "Your guess is too low, try again...Attempts remaining: 9" and for 87 "Your guess is too low, try again...Attempts remaining: 8" hints accordingly | Pass |
| 2 | Correct guess and attempt count | Guessed the secret number correctly on the sixth attempt | Win message and correct attempt count displayed | Correct! you guessed secret number...! You took 6 attempts to guess
Congratulations! You won! | Pass |
| 3 | Letter input | Entered `abc` as a guess | Invalid input message; attempts unchanged | Invalid input, enter digits only! | Pass |
| 4 | Blank input | Pressed Enter without entering a guess | Invalid input message; attempts unchanged | Invalid input, enter digits only! | Pass |
| 5 | Numbers outside the range | Entered `0` and `51` in Easy mode | Both inputs rejected; attempts unchanged | Enter a number from 1 to 50. | Pass |
| 6 | Easy difficulty | Selected Easy | Range 1–50 with 10 attempts | Level: Easy Mode: Classic Guess a number from 1 to 50. You have 10 attempts. | Passes |
| 7 | Medium difficulty | Selected Medium | Range 1–100 with 8 attempts | Level: Medium Mode: Classic Guess a number from 1 to 100. You have 8 attempts. | Pass |
| 8 | Hard difficulty | Selected Hard | Range 1–500 with 10 attempts | Level: Hard Mode: Classic Guess a number from 1 to 500. You have 10 attempts. | Pass |
| 9 | Attempts exhausted | Used all allowed attempts without guessing correctly | Game ends and reveals the secret number | Attempts remaining: 0 Game over! The secret number was 32. | Pass |
| 10 | Time Challenge timeout | Allowed the 60-second timer to expire | Timeout message displayed and secret number revealed | Time's up! You ran out of time. The secret number was 32. | Pass |
| 11 | Remaining time display | Played a round in Time Challenge mode | Remaining seconds displayed before each guess | Your guess is too high, try again... Attempts remaining: 9 Time remaining: 25 seconds | Pass |
| 12 | Invalid menus and Classic mode | Entered invalid difficulty and mode choices, then tested Classic mode | Invalid choices prompt again; Classic mode has no time limit | Invalid choice, please choose from 1, 2, and 3 | Pass |