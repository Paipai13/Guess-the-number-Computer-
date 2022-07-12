import random

def guess(x):
  random_number = random.randint(1,x)
  guess= 0
  while guess != random_number:
    guess=int(input(f'I\'m thinking of a number, guess a number between 1 and {x}: '))
    if guess < random_number:
      print("Too low, guess again! ")
    elif guess > random_number:
      print("Too high, guess again! ")

  print(f'Correct! The Number I was thinking of was  {random_number} ')
      
guess (10)

