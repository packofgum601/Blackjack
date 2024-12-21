## Overview
A simple command line implementation of the card game blackjack. It is written in Python and allows players to compete against a virtual dealer. The game is played using simple text based commands.

## Features
  - A complete deck of cards with suits (♠, ♥, ♦, ♣) and ranks (2–10, J, Q, K, A).
  - The deck is shuffled before each round.
  - Both the player and the dealer take turns based on standard Blackjack rules:
      - The player can choose to "Hit" (draw a card) or "Stand" (end their turn).
      - The dealer will automatically hit until their hand total reaches at least 17.
  - Cards are graphically represented in ASCII art for better visualization in the terminal.
  - The dealer's second card is hidden until the player's turn ends.
  - Scores are tracked across multiple rounds.
  - Clear feedback is provided after each round to indicate the winner and the updated scores.

  ## Prerequisites
   - Python 3.x
   - A Terminal/CLI

## How to Run
  - Clone this repository to your own personal device
  - run the file by using the command python ./blackjack.py
  - Have fun playing!


## Differences to Normal Blackjack
  - No betting (yet)
  - Ace cards always equal one (In blackjack, aces can equal 1 or 11)
