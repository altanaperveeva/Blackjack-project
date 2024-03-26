#Blackjack

import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(cards):
  return sum(cards)
  
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return(sum(cards))
    

def compare(your_score, computer_score):
  if your_score == computer_score:
    print("Draw")
  elif computer_score == 0:
    print("You lose(")
  elif your_score == 0:
    print("You win!")
  elif your_score > 21:
    print("You lose(")
  elif computer_score > 21:
    print("You win!")
  elif your_score > computer_score:
    print("You win!")
  elif computer_score > your_score:
    print("You lose(")



def play_game():
  your_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    your_cards.append(deal_card())
    computer_cards.append(deal_card())

   
  while not is_game_over:
    your_score = calculate_score(your_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if your_score == 0 or computer_score == 0 or your_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        your_cards.append(deal_card())
      else:
        is_game_over = True 
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"Your final hand: {your_cards}, final score: {your_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  compare(your_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
