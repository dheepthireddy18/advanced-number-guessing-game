import random
import time

# ---------- Settings ----------
DEBUG_SECRET = 32   # For testing, set to a number such as 42. Set back to None before your final commit.
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
  difficulty_level = input("Choose your difficulty level(please enter your choice (1-3)): ").strip()
  
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

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
while True:
  print("\nGame Mode:")
  print("1. Classic")
  print("2. Time Challenge(60 seconds)")

  game_mode = input("Choose your game mode(1-2): ").strip()

  if game_mode == "1":
    mode = "Classic"
    break
  elif game_mode == "2":
    mode = "Time Challenge"
    break
  else:
    print("Invalid choice. Please enter 1 or 2.")

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
# setting a range for selecting the random number
if DEBUG_SECRET is None:
  secret_num = random.randint(low, high)
else:
  secret_num = DEBUG_SECRET

attempts = 0
game_won = False
timed_out = False
start_time = time.time()

print(f"Level: {level}")
print(f"Mode: {mode}")
print(f"Guess a number from {low} to {high}.")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts and not timed_out:

  # to show the remaining time and stop if the deadline has passed.
  if mode == "Time Challenge":
    elapsed_time = time.time() - start_time
    seconds_left = TIME_LIMIT - elapsed_time
  
    if seconds_left <= 0:
      timed_out = True
      break
    print(f"Time remaining: {int(seconds_left)} seconds")

  entry = input("Guess a number: ").strip()
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

  # checking the time after a valid guess.
  # A guess submitted after the deadline cannot win.
  if mode == "Time Challenge":
    elapsed_time = time.time() - start_time

    if elapsed_time >= TIME_LIMIT:
      timed_out = True
      break

  # if the gussed number is valid and within the range, provide with appropriate hints to get to the actual number
  if guess < secret_num:
    print("Your guess is too low, try again...")
  elif guess > secret_num:
    print("Your guess is too high, try again...")
  # once the user gussed the number correct the loop ends and exits from the fils
  else:
    game_won = True
    print(f"Correct! you guessed secret number...! You took {attempts} attempts to guess")  
    break

  attempts_left = max_attempts - attempts
  print(f"Attempts remaining: {attempts_left}")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
if timed_out:
  print("Time's up! You ran out of time.")
  print(f"The secret number was {secret_num}.")
elif game_won:
  print("Congratulations! You won!")
else:
  print(f"Game over! The secret number was {secret_num}.")