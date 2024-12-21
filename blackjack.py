#game of blackjack using the CLI
#Classes:
    #card class
    #deck class
#Variables:
    #dealer's cards
    #player's cards
#functions
    #deal
    #shuffle
    #hit
    #stand
    #end of game
        #reveal dealer's card
        #compare scores

#imports
import random

import os
os.system('cls' if os.name == 'nt' else 'clear')

#constants
RANKS = ("2","3","4","5","6","7","8","9","10","K","Q","J","A")
VALUES = {"2":2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}
SUITS = ('♠', '♥', '♦', '♣')
TOP = "┌─────────┐"
BOTTOM = "└─────────┘"
SIDE = "│         │"

dealer_score = 0
player_score = 0


class Card:
    def __init__(self,  suit, rank ):
        #suit: suit of card
        self.suit = suit
       #rank: value written on the card (1-10,K,Q,J,A)
        self.rank = rank
        #value: value of card (K,Q,J = 10 and A = 1)
        self.value = VALUES[rank]
        #face_up: whether the card is faced up or down
        self.face_up = True

        if rank == "10":  # Ten is the only rank with two digits
            rank_right = rank
            rank_left = rank
        else:
            rank_right = rank + " "
            rank_left = " " + rank

        suit_line = f"│    {suit}    │"
        dealer_rank_line_left = f"│?        │"
        dealer_rank_line_right = f"│        ?│"
        dealer_suit_line = f"│    ?    │"
        rank_line_left = f"│{rank_left}       │"
        rank_line_right = f"│       {rank_right}│"
        self.suit_line = suit_line
        self.rank_line_left = rank_line_left
        self.rank_line_right = rank_line_right
        self.dealer_rank_line_left = dealer_rank_line_left
        self.dealer_rank_line_right = dealer_rank_line_right
        self.dealer_suit_line = dealer_suit_line


    def __str__ (self):
        if self.face_up == True:
            return f"{TOP}\n{self.rank_line_left}\n{SIDE}\n{self.suit_line}\n{SIDE}\n{self.rank_line_right}\n{BOTTOM}  "
        return f"{TOP}\n{self.dealer_rank_line_left}\n{SIDE}\n{self.dealer_suit_line}\n{SIDE}\n{self.dealer_rank_line_right}\n{BOTTOM}  "


    def getValue(self):
        return int(self.value)
    def getRank(self):
        return int(self.rank)

    def TurnCardOver(self):
        #turns card over (face up to face down or face down to face up)
        self.face_up = not self.face_up

class Deck:
    def __init__(self):
        #full_deck: the whole deck
        self.full_deck = [Card(suit,rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        #shuffles the deck
        random.shuffle(self.full_deck)

    def deal(self):
        #deals the first card in the array
        return self.full_deck.pop(0)

class Hand:
    def __init__(self,name):
        #name: player or dealer
        self.name = name
        #cards: list of cards in hand
        self.cards = []

    def add_card(self,added_card):
        #add a card to the hand
        self.cards.append(added_card)

    def reset_hand(self):
        #resets hand at the end of round
        self.cards = []


    def hand_total(self):
        #calculates the total score of hand
        total = 0
        for card in self.cards:
            total += card.value
        return total


#functions
#print_hands: prints each hand
def print_hands(hand_player, hand_dealer):
    def format_hand(cards):
        card_lines = [str(card).split('\n') for card in cards]
        formatted_lines = ['\t'.join(line) for line in zip(*card_lines)]
        return '\n'.join(formatted_lines)

    print("\nDealer's Hand:")
    print(format_hand(hand_dealer.cards))
    print("\nPlayer's Hand:")
    print(format_hand(hand_player.cards))
    print("\n")

#check score: checks if either hand is over 21
def check_score(player_hand, dealer_hand):
    if player_hand.hand_total() > 21 and dealer_hand < 21:
        return

def Hit(hand, deck):
    # add card to deck
    hand.add_card(deck.deal())
    return hand

def compare_scores(hand_player, hand_dealer):
    global player_score
    global dealer_score
    p_total = hand_player.hand_total()
    d_total = hand_dealer.hand_total()

    print_hands(hand_player, hand_dealer)

    print(f"Your total is {hand_player.hand_total()}\n")
    print(f"Dealer's total is {hand_dealer.hand_total()}\n")

    if d_total > 21:
        print("Dealer's total is over 21 \nYou Win!")
        player_score += 1
    elif d_total > p_total :
        print("Dealer's score was closer to 21 \nDealer wins!")
        dealer_score += 1
    elif d_total < p_total:
        print("Your score is closer 21 \n You win!")
        player_score += 1
    else:
        print("Tie!")




#players turn: all the logic for the player's turn
def player_turn(hand_player, hand_dealer, deck):
    stand = False
    outcome = True
    p_total = hand_player.hand_total()
    while p_total <= 21 and stand == False:
        print_hands(hand_player, hand_dealer)
        print(f"Your Total is {hand_player.hand_total()}")
        choice = input("Would you like to Hit or Stand? (H,S) \n")
        if choice == "H":
            hand_player = Hit(hand_player, deck)
            #recalculate total
            p_total = hand_player.hand_total()
            if p_total > 21:
                outcome = False

        if choice == "S":
            if p_total > 21:
                outcome = False

            print("Moving on to the Dealer's Turn")

            stand = True

    return outcome



    #player has a choice of hitting or standing

#dealer's turn: all the logic for the dealer's turn
def dealer_turn(hand_player, hand_dealer, deck):
    stand = False
    outcome = True
    p_total = hand_player.hand_total()
    d_total = hand_dealer.hand_total()

    #flip card
    hand_dealer.cards[1].TurnCardOver()

    #if total > 17, stand, else keep hitting until total is over 17
    while d_total < 17 :
        hand_dealer = Hit(hand_dealer, deck)
        d_total = hand_dealer.hand_total()

    compare_scores(hand_player, hand_dealer)



#main
def main():
    global player_score
    global dealer_score
    #greet player
    print("Welcome to Blackjack!")
    input("Press Enter to deal hands... \n")

    keep_playing = True

    while keep_playing == True:
        #create new deck
        deck = Deck()
        #shuffle deck
        deck.shuffle()
        print(f"Your score is {player_score}")
        print(f"Dealer's score is {dealer_score}")

        #create player and dealer hands
        hand_player = Hand("player")
        hand_dealer = Hand("dealer")

        #deal initial cards to player and dealer
        for i in range(2):
            #deal card to player
            hand_player.add_card(deck.deal())
            #deal card to dealer
            hand_dealer.add_card(deck.deal())
        #turn dealer's second card face down
        hand_dealer.cards[1].TurnCardOver()



        #start players turn and goes to dealer's turn when either the player decides to stand or their total is over 21
        if player_turn(hand_player, hand_dealer, deck):
            dealer_turn(hand_player, hand_dealer, deck)
        else:
            hand_dealer.cards[1].TurnCardOver()
            print_hands(hand_player, hand_dealer)
            print(f"Your total was {hand_player.hand_total()}, which is over 21 \n Dealer wins!")
            dealer_score += 1

        print("\n")
        play_again = input("Would you like to play again? (y/n) \n")
        if play_again == "n":
            keep_playing = False













main()


