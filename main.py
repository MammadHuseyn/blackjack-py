import random
import os
import time
import sys

from asciiArtGenerator import print_card
os.system('cls' if os.name == 'nt' else 'clear')

with open('blackjack.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

def clear_screen(myHand, raptorHand, crackerHand, dealerShownHand):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('blackjack.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    if myHand != 0:
        print(f"Your hand: {myHand}")
        print(f"Raptor's hand: {raptorHand}")
        print(f"Cracker's hand: {crackerHand}")
        print(f"Dealer's hand: {dealerShownHand}")

def print_text(text):
    print(text)
    time.sleep(1.5)
    clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)


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
    'A':[1,11], '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10,
}


usedCards = []
crackerHand = 0
myHand = 0
raptorHand = 0
dealerHand = 0
dealerShownHand = 0

dealerCard = ""

def add_card_to_hand(hand, card):
    if card == 'A':
        if hand + 11 <= 21:
            return hand + 11
        else:
            return hand + 1
    else:
        return hand + cards[card]

def deal_card(flag):
    global myHand, raptorHand, dealerHand, dealerShownHand, dealerCard, crackerHand
    number = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    affir = random.choice(['♠', '♥', '♦', '♣'])
    card = f"{number}{affir}"

    while card in usedCards:
        deal_card(flag)
        return

    usedCards.append(card)
    
    if flag == "player":
        myHand = add_card_to_hand(myHand, number)
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)

    elif flag == "raptor":
        raptorHand = add_card_to_hand(raptorHand, number)
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)
    elif flag == "cracker":
        crackerHand = add_card_to_hand(crackerHand, number)
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)

    elif flag == "0":
        dealerHand = add_card_to_hand(dealerHand, number)
        dealerShownHand = add_card_to_hand(dealerShownHand, number)
        print_card(str(number), affir)
        time.sleep(1.5)
        clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)
    else:
        dealerHand = add_card_to_hand(dealerHand, number)
        dealerCard = card


def should_hit(hand, opponent_hand, threshold=17):
    if opponent_hand <= 21:
        return hand < threshold or (hand < opponent_hand and opponent_hand - hand > 4)
    else:
        return hand < threshold




def play_game():
    usedCards.clear()
    global myHand, raptorHand, dealerHand, dealerShownHand, crackerHand
    myHand = 0
    raptorHand = 0
    dealerHand = 0
    crackerHand = 0
    dealerShownHand = 0
    myself = False
    raptor = False
    cracker = False


    for i in range(2):
        clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)
        print_text("Dealer shuffling the deck...")

        print_text("Dealer gives you a card...")
        deal_card("player")

        print_text("Dealer gives Raptor a card...")
        deal_card("raptor")

        print_text("Dealer gives Cracker a card...")
        deal_card("cracker")

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
            print_text("Raptor went over 21! Raptor lose!")
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

    while should_hit(crackerHand, myHand) == True and cracker == False:
        print_text("Cracker hits...")
        print_text("Dealer gives Cracker a card...")
        deal_card("cracker")
        if crackerHand > 21:
            print_text("Cracker went over 21! Cracker lose!")
            cracker = True
            break
        elif crackerHand == 21:
            print_text("Cracker got a blackjack! Cracker wins!")
            cracker = True
            break
        
    if raptor == True and myself == True and cracker == True:
        print("All players lost!\nDealer WINS!")
        return

    print_text("Dealer reveals her card...")
    print_card(dealerCard[0],dealerCard[1])
    dealerShownHand += cards[dealerCard[0]]
    time.sleep(1.5)
    clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)

    while dealerHand < 17:
        deal_card("0")


 #-----------------------------------------------------------------------------------------
    if dealerHand > 21:
        dealer = True
        if myself == False and raptor == False and cracker == False:
            print("All players win!")
        elif myself == False and raptor == True and cracker == True:
            print("Player WINS!")
        elif raptor == False and myself == True and cracker == True:
            print("Raptor WINS!")
        elif cracker == False and myself == True and raptor == True:
            print("Cracker WINS!")
        elif myself == True and raptor == False and cracker == False:
            print("Raptor and Cracker WIN!")
        elif myself == False and raptor == True and cracker == False:
            print("Player and Cracker WIN!")
        elif myself == False and raptor == False and cracker == True:
            print("Player and Raptor WIN!")

    elif dealerHand == 21:
        print("Dealer WINS!")

#-----------------------------------------------------------------------------------------


    elif dealerHand < 21:
        if myself == False and raptor == False and cracker == False:
            if myHand > dealerHand and raptorHand > dealerHand and crackerHand > dealerHand:
                print("All players win!")
            elif myHand < dealerHand and raptorHand < dealerHand and crackerHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
            elif myHand > dealerHand and raptorHand < dealerHand and crackerHand < dealerHand:
                print("Cracker and Raptor lose. Player and Dealer WIN!")
            elif myHand < dealerHand and raptorHand > dealerHand and crackerHand < dealerHand:
                print("Player and Cracker lose. Raptor and Dealer WIN!")
            elif myHand < dealerHand and raptorHand < dealerHand and crackerHand > dealerHand:
                print("Player and Raptor lose. Cracker and Dealer WIN!")
            elif myHand > dealerHand and raptorHand > dealerHand and crackerHand < dealerHand:
                print("Cracker lose. Player, Raptor and Dealer WIN!")
            elif myHand > dealerHand and raptorHand < dealerHand and crackerHand > dealerHand:
                print("Raptor lose. Player, Cracker and Dealer WIN!")
            elif myHand < dealerHand and raptorHand > dealerHand and crackerHand > dealerHand:
                print("Player lose. Raptor, Cracker and Dealer WIN!")
        elif myself == True and raptor == False and cracker == False:
            if raptorHand > dealerHand and crackerHand > dealerHand:
                print("Raptor and Cracker WIN!")
            elif raptorHand < dealerHand and crackerHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
            elif raptorHand > dealerHand and crackerHand < dealerHand:
                print("Cracker loses. Raptor and Dealer WIN!")
            elif raptorHand < dealerHand and crackerHand > dealerHand:
                print("Raptor loses. Cracker and Dealer WIN!")
        elif raptor == True and myself == False and cracker == False:
            if myHand > dealerHand and crackerHand > dealerHand:
                print("Player and Cracker WIN!")
            elif myHand < dealerHand and crackerHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
            elif myHand > dealerHand and crackerHand < dealerHand:
                print("Cracker loses. Player and Dealer WIN!")
            elif myHand < dealerHand and crackerHand > dealerHand:
                print("Player loses. Cracker and Dealer WIN!")
        elif cracker == True and myself == False and raptor == False:
            if myHand > dealerHand and raptorHand > dealerHand:
                print("Player and Raptor WIN!")
            elif myHand < dealerHand and raptorHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
            elif myHand > dealerHand and raptorHand < dealerHand:
                print("Raptor loses. Player and Dealer WIN!")
            elif myHand < dealerHand and raptorHand > dealerHand:
                print("Player loses. Raptor and Dealer WIN!")
        elif myself == True and raptor == True and cracker == False:
            if crackerHand > dealerHand:
                print("Cracker WINS!")
            elif crackerHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
        elif myself == True and cracker == True and raptor == False:
            if raptorHand > dealerHand:
                print("Raptor WINS!")
            elif raptorHand < dealerHand:
                print("All players lose. Only Dealer WINS!")
        elif raptor == True and cracker == True and myself == False:
            if myHand > dealerHand:
                print("Player WINS!")
            elif myHand < dealerHand:
                print("All players lose. Only Dealer WINS!")

#-----------------------------------------------------------------------------------------
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
clear_screen(myHand, raptorHand, crackerHand, dealerShownHand)

play_game()