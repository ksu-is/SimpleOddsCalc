def build_deck():
    # Create the starting deck
    deck = []
    # Numbered Cards
    for value in range(9):
        for suit in range(4):
            if suit == 0:
                deck.append(str(value + 2) + 'S')
            elif suit == 1:
                deck.append(str(value + 2) + 'H')
            elif suit == 2:
                deck.append(str(value + 2) + 'C')
            elif suit == 3:
                deck.append(str(value + 2) + 'D')
    # Named Cards
    for value in range(4):
        named_cards = ''
        if value == 0:
            named_cards = 'J'
        elif value == 1:
            named_cards = 'Q'
        elif value == 2:
            named_cards = 'K'
        elif value == 3:
            named_cards = 'A'
        for suit in range(4):
            if suit == 0:
                deck.append(named_cards + 'S')
            elif suit == 1:
                deck.append(named_cards + 'H')
            elif suit == 2:
                deck.append(named_cards + 'C')
            elif suit == 3:
                deck.append(named_cards + 'D')
    return deck

# For named cards (eg Ace or A), change to numerical value
def letter_to_value(card):
    if card[0] == 'A':
        card = str(14) + card[1]
    elif card[0] == 'K':
        card = str(13) + card[1]
    elif card[0] == 'Q':
        card = str(12) + card[1]
    elif card[0] == 'J':
        card = str(11) + card[1]
    return card

# function to get the users hole cards
def hole_cards():
    user_hand = []
    while len(user_hand) < 2:
        if len(user_hand) < 1:
            user_card = input("Enter the first hole card: ").upper()
            user_card = letter_to_value(user_card)
            user_hand.append(user_card)
        else:
            user_card = input("Enter the second hole card: ").upper()
            user_card = letter_to_value(user_card)
            user_hand.append(user_card)
    return user_hand

# function to get the board flop
def board_flop():
    flop_cards= []
    flop_input = input("Please enter the three flop cards (e.g. 2S 3S 4S)\nWhat is the flop?: ").upper()
    while len(flop_cards) < 2:
        if len(flop_input) == 8:
            flop_cards = flop_input.split()
        else:
            print("\nPlease enter the flop cards in the correct format.\n")
            flop_input = input("Please enter the three flop cards (e.g. 2S 3S 4S)\nWhat is the flop?: ").upper()
    for card in range(3):
        flop_cards[card] = letter_to_value(flop_cards[card])
    flop_cards.sort()
    return flop_cards

# calculate the odds of improving players hand to the target hand. If the opposing player is all-in on the turn, then use the 4 rule, otherwise use the 2 rule
def outs_calc(hole_cards, board_cards, target_hand, all_in_bet):
    deck = build_deck()
    all_cards = hole_cards + board_cards
    all_cards.sort()

    flop_or_turn = ''
    if len(all_cards) == 5:
        flop_or_turn = 'FLOP'
    else:
        flop_or_turn = 'TURN'

    for card in all_cards:
        deck.remove(card)
    if target_hand == 'STRAIGHT':

    if target_hand == 'FLUSH':
    
    if target_hand == 'FULL HOUSE':
    
    if target_hand == 'QUADS':

    if target_hand == 'STRAIGHT FLUSH':

    if target_hand == 'STRAIGHT OR FLUSH':