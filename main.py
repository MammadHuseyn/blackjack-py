import random
import os
import time
import sys

from asciiArtGenerator import print_card
os.system('cls' if os.name == 'nt' else 'clear')

with open('blackjack.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

def clear_screen(myHand, raptorHand, dealerShownHand):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('blackjack.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    if myHand != 0:
        print(f"Your hand: {myHand}")
        print(f"Raptor's hand: {raptorHand}")
        print(f"Dealer's hand: {dealerShownHand}")

def print_text(text):
    print(text)
    time.sleep(1.5)
    clear_screen(myHand, raptorHand, dealerShownHand)


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
    'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10,
}


usedCards = []
myHand = 0
raptorHand = 0
dealerHand = 0
dealerShownHand = 0

dealerCard = ""

def deal_card(flag):
    global myHand, raptorHand, dealerHand, dealerShownHand, dealerCard
    number = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    affir = random.choice(['♠', '♥', '♦', '♣'])
    card = f"{number}{affir}"

    while card in usedCards:
        deal_card(flag)
        return

    usedCards.append(card)
    
    if flag == "player":
        myHand += cards[number]
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, dealerShownHand)

    elif flag == "raptor":
        raptorHand += cards[number]
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, dealerShownHand)
    elif flag == "0":
        dealerHand += cards[number]
        dealerShownHand += cards[number]
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, dealerShownHand)
    else:
        dealerHand += cards[number]
        dealerCard = card


def should_hit(hand, opponent_hand, threshold=17):
    return hand < threshold or (hand < opponent_hand and opponent_hand - hand > 4)




def play_game():
    usedCards.clear()
    global myHand, raptorHand, dealerHand, dealerShownHand
    myHand = 0
    raptorHand = 0
    dealerHand = 0
    dealerShownHand = 0
    myself = False
    raptor = False


    for i in range(2):
        clear_screen(myHand, raptorHand, dealerShownHand)
        print_text("Dealer shuffling the deck...")

        print_text("Dealer gives you a card...")
        deal_card("player")

        print_text("Dealer gives Raptor a card...")
        deal_card("raptor")

        print_text("Dealer gives herself a card...")
        deal_card(str(i))

    choice = input("Do you want to hit or stand?: ")
    while choice.lower() == "hit" and myself == False:
        if choice.lower() == "hit":
            print_text("Dealer gives you a card...")
            deal_card("player")
            if myHand > 21:
                print_text("You went over 21! You lose!")
                myself = True
                break
            elif myHand == 21:
                print_text("You got a BLACKJACK! You are a Winner!")
                myself = True
                break
        else:
            print_text('Player stands...')
            break
        choice = input("Do you want to hit or stand?: ")


    while should_hit(raptorHand, myHand) == True and raptor == False:
        print_text("Raptor hits...")
        print_text("Dealer gives Raptor a card...")
        deal_card("raptor")
        if raptorHand > 21:
            print_text("Raptor went over 21! Raptors lose!")
            raptor = True
            break
        elif raptorHand == 21:
            print_text("Raptor got a blackjack! Raptor wins!")
            raptor = True
            break

    if raptor == False:
        print_text("Raptor stands...")
        print("Raptor:", end=" ")
        raptorsProvocation(raptorHand)
        
    if raptor == True and myself == True:
        print("Both players lost!\nDealer WINS!")
        return

    print_text("Dealer reveals her card...")
    print_card(dealerCard[0],dealerCard[1])
    dealerShownHand += cards[dealerCard[0]]
    time.sleep(1.5)
    clear_screen(myHand, raptorHand, dealerShownHand)

    while dealerHand < 17:
        deal_card("0")

    if dealerHand > 21:
        dealer = True
        if myself == False and raptor == False:
            print("Both player and Raptor wins!")
        elif myself == False and raptor == True:
            print("Player WINS!")
        elif raptor == False and myself == True:
            print("Raptor WINS!")

    elif dealerHand == 21:
        print("Dealer WINS!")

    else:
        if myself == False and raptor == False:
            if myHand > dealerHand and raptorHand > dealerHand:
                print("Both player and Raptor wins!")
            elif myHand > dealerHand and raptorHand < dealerHand:
                print("Player WINS!")
            elif myHand < dealerHand and raptorHand > dealerHand:
                print("Raptor WINS!")
            elif myHand < dealerHand and raptorHand < dealerHand:
                print("Both of player loses!\nDealer's hand is higher!\nDealer WINS!")
        elif myself == True and raptor == False:
            if raptorHand > dealerHand:
                print("Raptor WINS!")
            elif raptorHand < dealerHand:
                print("Raptor loses!\nDealer WINS!")
        elif myself == False and raptor == True:
            if myHand > dealerHand:
                print("Player WINS!")
            elif myHand < dealerHand:
                print("Player loses!\nDealer WINS!")



        elif myHand == dealerHand and raptorHand == dealerHand:
            print("It's a tie between all players and the dealer!")
        elif myHand == dealerHand and raptorHand < dealerHand:
            if myself == False:
                print("Player ties with Dealer! Raptor loses!")
            else:
                print("Player loses! Raptor loses!")
        elif myHand == dealerHand and raptorHand > dealerHand:
            if myself == False:
                print("Player ties with Dealer! Raptor wins!")
            else:
                print("Player loses! Raptor wins!")
        elif myHand < dealerHand and raptorHand == dealerHand:
            if raptor == False:
                print("Raptor ties with Dealer! Player loses!")
            else:
                print("Raptor loses! Player loses!")
        elif myHand > dealerHand and raptorHand == dealerHand:
            if myself == False:
                print("Player wins! Raptor ties with Dealer!")
            else:
                print("Player loses! Raptor ties with Dealer!")

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
clear_screen(myHand, raptorHand, dealerShownHand)

play_game()