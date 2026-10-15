import random

print("Welcome to the Number Guessing Game")
print("Goal: Guess the secret number")

# setting a range for selecting the random number
secret_num = random.randint(1,100)
attempts = 0

while True:
  entry = input("Guess a number: ")
  # to check whether the input is a digit if not ask for the new input again
  if not entry.isdigit():
    print("Invalid input, enter digits only!")
    continue
  # converting the input to integer
  guess = int(entry)
  # checking checking the input is within the range of gussed number range
  if guess < 1 or guess > 100:
    print("Enter a number from 1 to 100.")
    continue
  # incrementing the attempts for every valid guess 
  attempts += 1
  # if the gussed number is valid and within the range, provide with appropriate hints to get to the actual number
  if guess < secret_num:
    print("Your guess is too low, try again...")
  elif guess > secret_num:
    print("Your guess is too high, try again...")
  # once the user gussed the number correct the loop ends and exits from the fils
  elif guess == secret_num:
    print(f"Yayyy! you guessed secret number...! you took {attempts} attempts to guess")  
    break
