import random

AUTHOR = "Matthew Rakay"
APP_NAME = "Guessing Game"


def run():
  print("  welcome to the guessing game!")
  print("  Pick a number from 1 and 100")

  secret_number = random.randint(1, 100)
  attempts = 0

  while True:
    try:
      guess = int(input("  Pick your number: "))
      attempts += 1

      if guess < secret_number:
        print("  Too low try again.")
      elif guess > secret_number:
        print("  Too high try again.")
      else:
        return (
            f"YOU'RE THE WINNER! Hooray! Hooray! It took {attempts} guesses!"
        )
    except ValueError:
      print("  Please enter a valid number.")


if __name__ == "__main__":
  print(run())