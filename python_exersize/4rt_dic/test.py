import random

# Define the card ranks and suits
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠", "♥", "♦", "♣"]

# Select a random card from the deck
rank = random.choice(ranks)
suit = random.choice(suits)

# Define the ASCII art for the card
card = [
    "┌─────────┐",
    f"│ {rank:<2}      │",
    "│         │",
    "│         │",
    f"│    {suit}    │",
    "│         │",
    "│         │",
    f"│      {rank:>2} │",
    "└─────────┘"
]

# Display the card
for line in card:
    print(line)
