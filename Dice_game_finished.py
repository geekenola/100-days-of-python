from art import logo
from art import vs
import random
from game_data import data
from replit import clear

print(logo)
score=0
game_continues = True
account_b = random.choice(data)
while game_continues:
  account_a = account_b
  account_b = random.choice(data)
  while account_a== account_b:
    account_b = random.choice(data)
  
  def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  
  print(f"Against B: {format_data(account_b)}")
  
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  def check_answer(guess, a_follower_count, b_follower_count):
    if guess == "a":
      if a_follower_count > b_follower_count:
        return guess=='a'
      else:
        return guess=='b'
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  random.choice(data)random.choice(data)clear()  
  if is_correct:
    score+=1
    print(f"You're right!, Current score: {score}.")
  else:
    game_continues = False
    print(f"Sorry, that is wrong. final score : {score}")
    
  
  


