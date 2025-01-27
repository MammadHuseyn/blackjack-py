import random
import os
import time
import sys

from asciiArtGenerator import print_card
os.system('cls' if os.name == 'nt' else 'clear')

with open('blackjack.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('blackjack.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    if myHand != 0:
        print(f"Your hand: {myHand}")
    

def print_text(text):
    print(text)
    time.sleep(1.5)
    clear_screen()


raptor_winning_phrases = ["Play! You sucker!", "U can't beat me!",
                          "Miss ur mama?", "Hahaha", "I will beat ur ass",
                          "Go home and drink ur milk", "Suck my d*ck!"]
raptor_loosing_phrases = ["Don't be harsh on me", 
                          "I am really scared this time",
                          "Have a mercy!",
                          "Oh GOD!", "GOSH", "ARE U CHEATING?", "DO NOT LOOK AT ME",
                          "Jesus Christ!"]

def raptorsProvocation(Hand):
    if Hand>18:
        cringeRate = random.randint(0, 100)
        if cringeRate > 80:
            print_text(random.choice(raptor_winning_phrases))
        else:
            print_text(random.choice(raptor_loosing_phrases))

    else:
        cringeRate = random.randint(0, 100)
        if cringeRate > 80:
            print_text(random.choice(raptor_loosing_phrases))
        else:
            print_text(random.choice(raptor_winning_phrases))

cards = {
    'A':1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10,
}
usedCards = []
myHand = 0
raptorHand = 0
dealerHand = 0

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


def should_hit(hand, opponent_hand, threshold=17):
    # Hit if hand is below threshold or if opponent's hand is significantly higher
    return hand < threshold or (hand < opponent_hand and opponent_hand - hand > 4)




def play_game():
    usedCards.clear()
    global myHand, raptorHand, dealerHand
    myHand = 0
    raptorHand = 0
    dealerHand = 0

    raptor = False
    dealer = False

    myCount = 0
    raptorCount = 0
    dealerCount = 0

    for i in range(2):
        clear_screen()
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
            if myHand > 21:
                print_text("You went over 21! You lose!")
                break
            if myHand == 21:
                print_text("You got a blackjack! You win!")
                break
            myCount = 0
        else:
            myCount += 1
        
        if raptor == False:
            print("Raptor:", end=" ")
            raptorsProvocation(raptorHand)

        if should_hit(raptorHand, myHand) and raptor == False:
            print_text("Dealer gives Raptor a card...")
            deal_card("raptor")
            if raptorHand > 21:
                print_text("Raptor went over 21! Raptors lose!")
                raptor = True
            elif raptorHand == 21:
                print_text("Raptor got a blackjack! Raptor wins!")
                break
            raptorCount = 0
        elif raptor == False:
            print_text("Raptor stands.")
            raptorCount += 1
        
        if should_hit(dealerHand, myHand) and dealer == False:
            print_text("Dealer gives herself a card...")
            deal_card("dealer")
            if dealerHand > 21:
                print_text("Dealer went over 21! Dealer lose!")
                dealer = True
            elif dealerHand == 21:
                print_text("Dealer got a blackjack! Dealer wins!")
                break
            dealerCount = 0
        elif dealer == False:
            print_text("Dealer stands.")
            dealerCount += 1


        if dealer and raptor:
            print_text("Dealer and Raptor both lose, you win!")
            break

        if myCount >= 2 and raptorCount >= 2 and dealerCount >= 2 and raptor == False and dealer == False:
            print_text("Everyone stands. Let's see who wins!")
            print_text("Revealing the cards...")
            if myHand > raptorHand and myHand > dealerHand:
                print("You win!")
            elif raptorHand > myHand and raptorHand > dealerHand:
                print("Raptor wins!")
            elif dealerHand > myHand and dealerHand > raptorHand:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            break
        elif myCount >= 2 and raptorCount >= 2 and raptor == False and dealer == True:
            print_text("You and Raptor both stands. Let's see who wins!")
            print_text("Revealing the cards...")
            if myHand > raptorHand:
                print("You win!")
            elif raptorHand > myHand:
                print("Raptor wins!")
            else:
                print("It's a tie!")
            break
        elif myCount >= 2 and dealerCount >= 2 and raptor == True and dealer == False:
            print("You and Dealer both stands. Let's see who wins!")
            print("Revealing the cards...")
            if myHand > dealerHand:
                print("You win!")
            elif dealerHand > myHand:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            break

    with open('dealer.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

    print("If you want to play again, press 1. If you want to exit, press 2.")
    choice = input("Your choice: ")
    if choice == "1":
        play_game()
    else:
        print("Thanks for playing!")
        sys.exit(0)      
    
input("Press Enter to start the game...")
clear_screen()

play_game()

