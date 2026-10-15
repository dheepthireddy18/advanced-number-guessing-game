import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")
print("Goal: Guess the secret number")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
while True:
  print("Difficulty levels:")
  print("1. Easy: numbers ranging from 1-50 with 10 attempts atmost")
  print("2. Medium: numbers ranging from 1-100 with 8 attempts atmost")
  print("3. Hard: numbers ranging from 1-500 with 10 attempts atmost")
  difficulty_level = input("Choose your difficulty level(please enter your choice (1-3)): ")
  
  if difficulty_level == "1":
    low = 1
    high = 50
    max_attempts = 10
    level = "Easy"
    break
  elif difficulty_level == "2":
    low = 1
    high = 100
    max_attempts = 8
    level = "Medium"
    break
  elif difficulty_level == "3":
    low = 1
    high = 500
    max_attempts = 10
    level = "Hard"
    break
  else:
    print("Invalid choice, please choose from 1, 2, and 3")

# setting a range for selecting the random number
if DEBUG_SECRET is None:
  secret_num = random.randint(low, high)
else:
  secret_num = DEBUG_SECRET

attempts = 0
game_won = False

while attempts < max_attempts:
  entry = input("Guess a number: ")
  # to check whether the input is a digit if not ask for the new input again
  if not entry.isdigit():
    print("Invalid input, enter digits only!")
    continue
  # converting the input to integer
  guess = int(entry)
  # checking checking the input is within the range of gussed number range
  if guess < low or guess > high:
    print(f"Enter a number from {low} to {high}.")
    continue
  # incrementing the attempts for every valid guess 
  attempts += 1

  # if the gussed number is valid and within the range, provide with appropriate hints to get to the actual number
  if guess < secret_num:
    print("Your guess is too low, try again...")
  elif guess > secret_num:
    print("Your guess is too high, try again...")
  # once the user gussed the number correct the loop ends and exits from the fils
  else:
    print(f"Correct! you guessed secret number...! You took {attempts} attempts to guess")  
    game_won = True
    break

  attempts_left = max_attempts - attempts
  print(f"Attempts remaining: {attempts_left}")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
if not game_won:
    print(f"Game over! The secret number was {secret_num}.")