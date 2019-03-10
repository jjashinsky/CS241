import random
from random import randint

playAgain = "yes"

print("Welcome to the number guessing game!")
seedValue = input("Enter random seed: ")
random.seed(seedValue)

while playAgain == "yes":
   guess = 0
   numOfGuesses = 0
   num = randint(1,100)
   while guess != num:
       guess = int(input("\nPlease enter a guess: "))
       numOfGuesses +=1
       if guess < num:
           print("Higher")
       elif guess > num:
           print("Lower")
       else:
           print("Congratulations. You guessed it!")
           print("It took you {} guesses.\n" .format(numOfGuesses))
   playAgain = input("Would you like to play again (yes/no)? ")
print("Thank you. Goodbye.")
  