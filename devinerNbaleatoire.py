import random
#print("Welcome to Guess The Number !")
print("The rules are simple. I will think of a number and you try to guess it.")
#g�n�rer un num�ro al�atoire
isGuessRight = False
number = random.randint(1,10)
print(number)
guess = input("Guess a number between 1 and 10: ")
print("You guessed {}. That is right! You win!".format(guess))

while isGuessRight != True:
  guess = input("Guess a number between 1 and 10: ")
  if int(guess) == number:
    print("You guessed {}. That is right! You win!".format(guess))
    isGuessRight = True
  else:
    print("You guessed {}. Sorry, that isn t it. Try again.".format(guess))
