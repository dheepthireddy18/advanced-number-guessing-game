import random

print("Welcome to the Number Guessing Game")
print("Goal: Guess the secret number")

secret_num = random.randint(1,100)
attempts = 0

while True:
  entry = input("Guess a number: ")
  if not entry.isdigit():
    print("Invalid input, enter digits only!")
    continue
  guess = int(entry)
  if guess < 1 or guess > 100:
    print("Enter a number from 1 to 100.")
    continue
  attempts += 1
  if guess < secret_num:
    print("Your guess is too low, try again...")
  elif guess > secret_num:
    print("Your guess is too high, try again...")
  elif guess == secret_num:
    print(f"Yayyy! you guessed secret number...! you took {attempts} attempts to guess")  
    break
