import random
from replit import clear
from  blackjackLogo import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace can be 11 or 1, and 10,10,10 are Jack, Queen and King

def deal_hand():
    return random.choices(cards, k=2)

def get_final_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        return get_final_score(hand)
    if score == 21 and len(hand) == 2:
        return 0
    return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Its a Draw!!"
    elif c_score == 0:
        return "Computer looses as Player has Blackjack!"
    elif u_score == 0:
        return "Player looses as Computer has Blackjack!"
    elif u_score > 21:
        return "You went over. You lose 😤"
    elif c_score > 21:
        return "Computer went over. You win!!"
    elif u_score > c_score:
        return "You win!!"
    else:
        return "You Loose!!"


def play_blackjack():
  print(logo)
  your_hand = deal_hand()
  computer_hand = deal_hand()
  game_over = False 
  while not game_over:
    your_score = get_final_score(your_hand)
    computer_score = get_final_score(computer_hand)
    print(f"Your Cards: {your_hand}, Current score is: {your_score}")
    print(f"Computer's First Card is: {computer_hand[0]}")
    if your_score == 0 or computer_score == 0 or your_score > 21:
      game_over = True
    else:
      deal_again = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
      if deal_again == 'y':
        your_hand.append(random.choice(cards))
      else:
        game_over = True
  while computer_score != 0 and computer_score < 17:
    computer_hand.append(random.choice(cards))
    computer_score = get_final_score(computer_hand)

  print(f"Your final hand is: {your_hand} and final score is: {your_score} ")
  print(f"Computers final hand is: {computer_hand} and final score is: {computer_score} ")
  print(compare(your_score,computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower() == 'y':
  clear()
  play_blackjack()
print("Thanks for choosing to play Blackjack, see you next time!!!")

    
