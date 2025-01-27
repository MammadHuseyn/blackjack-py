import random
import os
import time

from asciiArtGenerator import print_card
os.system('cls' if os.name == 'nt' else 'clear')

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
    time.sleep(1.5)
    clear_screen()

def deal_card(flag):
    global myHand, raptorHand, dealerHand
    number = random.choice(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])
    affir = random.choice(['♠', '♥', '♦', '♣'])
    card = f"{number}{affir}"

    if card in usedCards:
        deal_card(flag)
    else:
        usedCards.append(card)
    
    if flag == "player":
        myHand += cards[number]
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen()

    elif flag == "raptor":
        raptorHand += cards[number]
    else:
        dealerHand += cards[number]


for i in range(2):
    print_text("Dealer shuffling the deck...")

    print_text("Dealer gives you a card...")
    deal_card("player")

    print_text("Dealer gives Raptor a card...")
    deal_card("raptor")

    print_text("Dealer gives herself a card...")
    deal_card("dealer")



while True:
    choice = input("Do you want to hit or stand?: ")
    if choice.lower() == "hit":
        print_text("Dealer gives you a card...")
        deal_card("player")
        

