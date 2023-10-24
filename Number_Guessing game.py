#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo

# Allow the player to submit a guess for a number between 1 and 100.
from random import randint
the_number = randint(1,100)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
def game_func_easy():
  global the_number
  user_win_or_lost=False
  count=10
  while user_win_or_lost==False:
    print('I am thinking a number between 1 to 100 inclusively.')
    
    print(f'You have {count} guesses.')
    count-=1
    users_number = int(input("make a guess: "))
    if users_number > the_number:
      print("Too high.")
    elif users_number < the_number:
      print('too low.')
    else:
      print(f"You got it! The number was {the_number}.")
      user_win_or_lost = True
    if count==0:
      print("You ran out of guesses. You lost ")
      user_win_or_lost = True
def game_func_hard():
  global the_number
  user_win_or_lost=False
  count=5
  while user_win_or_lost==False:
    print('I am thinking a number between 1 to 100 inclusively.')
    
    print(f'You have {count} guesses.')
    count-=1
    users_number = int(input("make a guess: "))
    if users_number > the_number:
      print("Too high.")
    elif users_number < the_number:
      print('too low.')
    else:
      print(f"You got it! The number was {the_number}.")
      user_win_or_lost = True
    if count==0:
      print("You ran out of guesses. You lost ")
      user_win_or_lost = True


      

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
play_again = True
while play_again == True:
  def welcome():
    print(logo)
    print("Welcome to the Number guessing game! ")
  level=input("Choose a difficulty level: easy or hard? ")
  if level == 'easy':
    game_func_easy()
  elif level == 'hard':
    game_func_hard()
  else:
    print("Please choose a valid difficulty level.")
  cont=input("Do you want to play again? Type 'yes' or 'no'. ")
  if cont == 'yes':
    play_again=True
  else:
    play_again=False
  if play_again == False:
    print("Thanks for playing!")