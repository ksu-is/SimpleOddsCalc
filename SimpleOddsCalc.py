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
        card = str(1) #+ card[1]
    elif card[0] == 'K':
        card = str(13) #+ card[1]
    elif card[0] == 'Q':
        card = str(12) #+ card[1]
    elif card[0] == 'J':
        card = str(11) #+ card[1]
    return card

# function to get the users hole cards
def hole_cards():
    user_hand = []
    while len(user_hand) < 2:
        if len(user_hand) < 1:
            user_card = input("Enter the first hole card: ").upper()
            #user_card = letter_to_value(user_card)
            user_hand.append(user_card)
        else:
            user_card = input("Enter the second hole card: ").upper()
            #user_card = letter_to_value(user_card)
            user_hand.append(user_card)
    return user_hand

# function to get the board state
def board_state():
    flop_cards= []
    flop_input = input("Please enter the board state (2s 3s...): ").upper()
    while len(flop_cards) < 2:
        if len(flop_input) == 8:
            flop_cards = flop_input.split()
        elif len(flop_input) == 11:
            flop_cards = flop_input.split()
        else:
            print("\nPlease enter the flop cards in the correct format.\n")
            flop_input = input("Please enter the board state (2s 3s...): ").upper()
    for card in range(len(flop_cards)):
        flop_cards[card] = letter_to_value(flop_cards[card])
    flop_cards.sort()
    return flop_cards

# calculate the odds of improving players hand to the target hand. If the opposing player is all-in on the turn, then use the 4 rule, otherwise use the 2 rule
def outs_calc(hole_cards, board_cards, target_hand, all_in_bet = False):
    deck = build_deck()
    all_cards = hole_cards + board_cards
    all_cards.sort()
    num_of_outs = 0
    
    if target_hand == 'STRAIGHT':
        # Get the values for the outs
        straight_outs = straight_check(all_cards)
        # count the number of outs
        for out in straight_outs:
            for card in deck:
                if str(out) == card[0]:
                    num_of_outs += 1
        # remove the card seen from the deck
        for card in all_cards:
            deck.remove(card)
        # calculate via the seen cards method and return
        return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    """ if target_hand == 'FLUSH':
    
    if target_hand == 'FULL HOUSE':
    
    if target_hand == 'QUADS':

    if target_hand == 'STRAIGHT FLUSH':

    if target_hand == 'STRAIGHT OR FLUSH':
    """

def straight_check(visible_cards):
    outs_list = []
    value_list = []
    # get the values to look for
    for card in visible_cards:
        value_list.append(int(card[0]))
    # check to see if there is an open ended draw and return the two values
    # we want to run the loop twice for the flop and three times for the turn
    # 5-3=2 and 6-3=3
    # For open ended we see if the next card is consecutive, and if the 3rd card
    # value is +3
    for card in range((len(visible_cards) - 3)):
        if value_list[card] == value_list[card + 3] - 3\
             and value_list[card] == value_list[card + 1] - 1:
            outs_list.append(value_list[card] - 1)
            outs_list.append(value_list[card + 3] + 1)
            return outs_list
            break
    # Checking for gutshot
    # because we know the user is looking for a straight and the
    # list is ordered, we can look for the first consecutive
    # pair and find the middle value (next value) to return
    for card in range(len(visible_cards) - 1):
        if value_list[card] == value_list[card + 1] - 1:
            outs_list.append(value_list[card + 1] + 1)
            return outs_list
            break

# test_list = ['2h', '4h', '6h', '6h', '7h']
# print(straight_check(test_list))

hole_cards = hole_cards()
board = board_state()
print(outs_calc(hole_cards, board, 'STRAIGHT'))

# print(outs_calc(['2H', '3H'], ['4H', '5H', '7H'], 'STRAIGHT'))


