import random
import os
import time

from asciiArtGenerator import print_card

cards = {
    'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10,
}


usedCards = []

myHand = 0
raptorHand = 0
dealerHand = 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    if myHand != 0:
        print(f"Your hand: {myHand}")
    

def print_text(text):
    print(text)
    time.sleep(1)
    clear_screen()

def deal_card(flag):
    card = random.choice(list(cards.keys()))
    french = random.choice(['♠', '♥', '♦', '♣'])
    if card in usedCards:
        deal_card()
    else:
        usedCards.append(card)
        return card
    if flag == "player":
        myHand += cards[card]
        print_card(str(card), french)


print_text("Dealer shuffling the deck...")
print_text("Dealer gives you a card...")
print_text("Dealer gives Raptor a card...")
print_text("Dealer gives herself a card...")





