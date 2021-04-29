import time
import os

def build_deck():
    # Create the starting deck
    deck = []
    # Numbered Cards
    for value in range(8):
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
    for value in range(5):
        named_cards = ''
        if value == 0:
            named_cards = 'T'
        elif value == 1:
            named_cards = 'J'
        elif value == 2:
            named_cards = 'Q'
        elif value == 3:
            named_cards = 'K'
        elif value == 4:
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

# function to get the users hole cards
def hole_cards():
    user_hand = []
    deck = build_deck()
    while len(user_hand) < 2:
        while len(user_hand) < 1:
            user_card = input("Enter the first hole card: ").upper()
            if user_card in deck:
                deck.remove(user_card)
                user_hand.append(user_card)
            else:
                print("\nEntered card has already been selected, or is not a card. Try Again.\n")
                time.sleep(0.5)
        while len(user_hand) < 2:
            user_card = input("\nEnter the second hole card: ").upper()
            if user_card in deck:
                user_hand.append(user_card)
            else:
                print("\nEntered card has already been selected, or is not a card. Try Again.\n")
                time.sleep(0.5)
    return user_hand

# function to get the board state
def board_state(hole_cards):
    flop_cards= []
    deck = build_deck()
    
    while True:
        round_state = input("Are we at the flop or the turn? (\"Flop\" or \"Turn\"): ").upper()
        if round_state.startswith("F"):
            print("Enter the three Flop cards")
            while len(flop_cards) < 3:
                user_card = input("\nCard " + str(len(flop_cards) + 1) + ": ").upper()
                if user_card in deck and user_card not in hole_cards:
                    flop_cards.append(user_card)
                else:
                    print("\nEntered card has already been selected, or is not a card. Try Again.\n")
                    time.sleep(0.5)
            break
        elif round_state.startswith("T"):
            print("Enter the three Flop cards and the Turn card")
            while len(flop_cards) < 4:
                user_card = input("\nCard " + str(len(flop_cards) + 1) + ": ").upper()
                if user_card in deck and user_card not in hole_cards:
                    flop_cards.append(user_card)
                else:
                    print("\nEntered card has already been selected, or is not a card. Try Again.\n")
                    time.sleep(0.5)
            break
        else:
            print("\nThat is not an accepted input.\n")
            time.sleep(0.5)
    return flop_cards

def target_hand():
    while True:
        user_selection = input("Enter the target hand:\n1 : STRAIGHT\n2 : FLUSH\n"
        + "3 : FULL HOUSE\n4 : STRAIGHT OR FLUSH\n5 : STRAIGHT FLUSH\n6 : QUADS\n"
        + "7 : PAIR ANY\n: ")
        if user_selection == '1':
            return 'STRAIGHT'
        elif user_selection == '2':
            return 'FLUSH'
        elif user_selection == '3':
            return 'FULL HOUSE'
        elif user_selection == '4':
            return 'STRAIGHT OR FLUSH'
        elif user_selection == '5':
            return 'STRAIGHT FLUSH'
        elif user_selection == '6':
            return 'QUADS'
        elif user_selection == '7':
            return 'FLUSH'
        else:
            print('Try Again\n')
            time.sleep(0.5)

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
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    elif target_hand == 'FLUSH':
        suit = flush_check(all_cards)
        for card in all_cards:
            deck.remove(card)
        for card in deck:
            if suit == card[1]:
                num_of_outs += 1
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    elif target_hand == 'FULL HOUSE':
        num_of_outs = full_house_check(all_cards)
        # remove the card seen from the deck
        for card in all_cards:
            deck.remove(card)
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    elif target_hand == 'STRAIGHT OR FLUSH':
        straight_outs = straight_check(all_cards)
        suit = flush_check(all_cards)
        outs = []
        # count the number of outs
        for out in straight_outs:
            for card in deck:
                if str(out) == card[0]:
                    outs.append(card)
        for card in deck:
            if suit == card[1]\
                 and card not in outs\
                 and card not in all_cards:
                outs.append(card)
        for card in all_cards:
            deck.remove(card)
        num_of_outs = len(outs)
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    elif target_hand == 'STRAIGHT FLUSH':
        straight_outs = straight_check(all_cards)
        suit = flush_check(all_cards)
        outs = []
        for out in straight_outs:
            for card in deck:
                if str(out) == card[0]\
                    and card[1] == suit:
                    outs.append(card)
        for card in all_cards:
            deck.remove(card)
        num_of_outs = len(outs)
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    elif target_hand == 'QUADS':
        values = ""
        for card in all_cards:
            values += card[0]
        for value in values:
            if values.count(value) == 3:
                for card in all_cards:
                    deck.remove(card)
                num_of_outs = 1
                # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')
    
    elif target_hand == 'PAIR ANY':
        values = ""
        for card in all_cards:
            values += card[0]
        for card in deck:
            if card[0] in values and card not in all_cards:
                num_of_outs += 1
        for card in all_cards:
                    deck.remove(card)
        # return (str(round(num_of_outs/len(deck)*100, 2)) + '%')

    if all_in_bet == False:
        return (str(round(num_of_outs/len(deck)*100, 2)) + '%')
    elif all_in_bet == True:
        if len(board_cards) == 3:
            return str(round((num_of_outs / len(deck) * 100)
                + (num_of_outs / (len(deck) - 1) * 100), 2)) + '%'
        elif len(board_cards) == 4:
            return (str(round(num_of_outs/len(deck)*100, 2)) + '%')


def straight_check(visible_cards):
    outs_list = []
    value_list = []
    num_of_outs = 0
    # get the values to look for
    for card in visible_cards:
        if card[0] == 'A':
            value_list.append(14)
            value_list.append(1)
        elif card[0] == 'T':
            value_list.append(10)
        elif card[0] == 'J':
            value_list.append(11)
        elif card[0] == 'Q':
            value_list.append(12)
        elif card[0] == 'K':
            value_list.append(13)
        else:
            value_list.append(int(card[0]))
        value_list.sort()
    # check to see if there is an open ended draw and return the two values
    # we want to run the loop twice for the flop and three times for the turn
    # 5-3=2 and 6-3=3
    # For open ended we see if the next card is consecutive, and if the 3rd card
    # value is +3
    for card in range((len(visible_cards) - 3)):
        if value_list[card] == value_list[card + 3] - 3\
             and value_list[card] == value_list[card + 1] - 1\
             and value_list[card] == value_list[card + 2] - 2:
            outs_list.append(value_list[card] - 1)
            if (value_list[card + 3] + 1) == 14:
                outs_list.append(1)
            else:
                outs_list.append(value_list[card + 3] + 1)
            for value in range(len(outs_list)):
                if outs_list[value] == 1:
                    outs_list[value] = 'A'
                elif outs_list[value] == 10:
                    outs_list[value] = 'T'
                elif outs_list[value] == 11:
                    outs_list[value] = 'J'
                elif outs_list[value] == 12:
                    outs_list[value] = 'Q'
                elif outs_list[value] == 13:
                    outs_list[value] = 'K'
            return outs_list
    # Checking for gutshot
    # because we know the user is looking for a straight and the
    # list is ordered, we can look for the first consecutive
    # pair and find the middle value (next value) to return
    for card in range(len(visible_cards) - 1):
        if value_list[card] == value_list[card + 1] - 1:
            outs_list.append(value_list[card + 1] + 1)
            for value in range(len(outs_list)):
                if outs_list[value] == 1:
                    outs_list[value] = 'A'
                elif outs_list[value] == 10:
                    outs_list[value] = 'T'
                elif outs_list[value] == 11:
                    outs_list[value] = 'J'
                elif outs_list[value] == 12:
                    outs_list[value] = 'Q'
                elif outs_list[value] == 13:
                    outs_list[value] = 'K'
            return outs_list

def flush_check(visible_cards):
    # a list with the count of each suit
    suits_list = []
    # join the list so we can count the number of suits and 
    # append them to the suits_list
    list_join = "".join(visible_cards)
    suits_list.append(list_join.count('S'))
    suits_list.append(list_join.count('H'))
    suits_list.append(list_join.count('C'))
    suits_list.append(list_join.count('D'))
    # find the index of the highest number of suits
    max_value = max(suits_list)
    max_index = suits_list.index(max_value)
    # return the character of the highest num of suits
    if max_index == 0:
        return 'S'
    elif max_index == 1:
        return 'H'
    elif max_index == 2:
        return 'C'
    elif max_index == 3:
        return 'D'

def full_house_check(visible_cards):
    values = ""
    for card in visible_cards:
        values += card[0]
    for value in values:
        if values.count(value) == 2:
            return 4
        elif values.count(value) == 3:
            return 9

all_in_check = False
    
hole_cards_list = hole_cards()
print()
time.sleep(0.5)
board = board_state(hole_cards_list)
print()
time.sleep(0.5)
target_hand = target_hand()
print()
time.sleep(0.5)
opp_all_in = input("Is your opponent all_in?: (y/n): ").upper()
if opp_all_in.startswith("Y"):
    all_in_check = True
odds = outs_calc(hole_cards_list, board, target_hand, all_in_check)
os.system("cls||clear")
print("\nThe odds that the next card will improve your had to the target hand,",
 "\n-", target_hand,"-", "is", odds)

while True:
    another_hand = input("\nWould you like to see another hand? (y/n): ")
    if another_hand.startswith('y'):
        os.system("cls||clear")
        hole_cards = hole_cards()
        print()
        board = board_state()
        print()
        target_hand = target_hand()
        odds = outs_calc(hole_cards, board, target_hand)
        print("\nThe odds that the next card will improve your had to the target hand,",
        "\n-", target_hand,"-", ", is", odds)
    elif another_hand.startswith('n'):
        print("\nGood Luck!")
        break
    else:
        print("Sorry, seems like you are indecisive...")