#SairajPulaparthi
#BlackJack Project


#import random
#define the variables here
import random
from p1_random import P1Random
rng = P1Random()
gameNum = 0
gameTied = 0
gamePlay = 0
userChoice = 0
playerWins = 0
playerScore = 0
dealerScore = 0
dealerWins = 0
newGame = True
#start the while statement equal to true
while True:
#start the if statements to keep track of the games and print the card numbers
        if newGame:
            newGame = False
            gameNum += 1
            gamePlay = gameNum - 1
            print(f"START GAME #{gameNum}")
            card =  rng. next_int(13) + 1
            if card == 1:
                print("\nYour card is a ACE!")
                playerScore += card
            elif card == 11:
                print("\nYour card is a JACK!")
                playerScore += 10
            elif card == 12:
                print("\nYour card is a QUEEN!")
                playerScore += 10
            elif card == 13:
                print("\nYour card is a KING!")
                playerScore += 10
            else:
                print(f"\nYour card is a {card}!")
                playerScore += card
            print(f"Your hand is: {playerScore}\n")
            print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
            user = int(input("Choose an option: "))
#control the out of bounds for the user input outside the range of 1-4
        if user < 1 or user > 4:
            print("\nInvalid input!\n\nPlease enter an integer value between 1 and 4.\n")
            print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
            user = int(input("Choose an option: "))
#start the if statements for when the user has inputted a function
        elif user == 1:
            card = rng. next_int(13) + 1
            if card == 1:
                print("\nYour card is a ACE!")
                playerScore += card
                print(f"Your hand is: {playerScore}\n")
            elif card == 11:
                    print("\nYour card is a JACK!")
                    playerScore += 10
                    print(f"Your hand is: {playerScore}\n")
            elif card == 12:
                    print("\nYour card is a QUEEN!")
                    playerScore += 10
                    print(f"Your hand is: {playerScore}\n")
            elif card == 13:
                    print("\nYour card is a KING!")
                    playerScore += 10
                    print(f"Your hand is: {playerScore}\n")
            else:
                    print(f"\nYour card is a {card}!")
                    playerScore += card
                    print(f"Your hand is: {playerScore}\n")
            if playerScore == 21:
                    print("BLACKJACK! You win!\n")
                    playerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
            elif playerScore > 21:
                    print("You exceeded 21! You lose.\n")
                    dealerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
            elif dealerScore > 21:
                    print(f"\nDealer's hand: {dealerScore}")
                    print(f"Your hand is: {playerScore}\n")
                    print("You win!\n")
                    playerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
            elif dealerScore == 21:
                    print(f"\nDealer's hand: {dealerScore}")
                    print(f"Your hand is: {playerScore}\n")
                    print("Dealer wins!\n")
                    dealerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
            else:
                    print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
                    user = int(input("Choose an option: "))
#hold the cards for when user inputted 2
        elif user == 2 :
                dealerCards = rng.next_int(11) + 16
                dealerScore += dealerCards
                print(f"\nDealer's hand: {dealerScore}")
                print(f"Your hand is: {playerScore}\n")
                if dealerScore > playerScore and dealerScore <= 21:
                    print("Dealer wins!\n")
                    dealerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
                elif dealerScore > 21:
                    print("You win!\n")
                    playerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
                elif dealerScore == playerScore:
                    print("It's a tie! No one wins!\n")
                    gameTied += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
                elif playerScore > dealerScore and playerScore < 21:
                    print("You win!\n")
                    playerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
                elif playerScore == 21:
                    print("BLACKJACK! You win!\n")
                    playerWins += 1
                    playerScore = 0
                    dealerScore = 0
                    newGame = True
                else:
                    newGame = True
#print the statistics out when for pressed 3
        elif user == 3:
            print(f"\nNumber of Player wins: {playerWins}")
            print(f"Number of Dealer wins: {dealerWins}")
            print(f"Number of tie games: {gameTied}")
            print(f"Total # of games played is: {gamePlay}")
            decimal = float(playerWins)
            percent = decimal / float(gamePlay)
            percentage= percent *100.0
            print(f"Percentage of Player wins: {percentage:.1f}%\n")
            print("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n")
            user = int(input("Choose an option: "))
#break the while looop when 4 is pressed.
        elif user == 4:

            break




