## Project Euler Q54 Solution
## How many hands does Player 1 win in the game of poker?
def split_hands(data):
    player1_hands = []
    player2_hands = []

    lines = data.strip().split('\n')
    for line in lines:
        cards = line.split()
        player1_hand = cards[:5]
        player2_hand = cards[5:]
        player1_hands.append(player1_hand)
        player2_hands.append(player2_hand)

    return player1_hands, player2_hands

# Example usage
with open('0054_poker.txt', 'r') as file:
    data = file.read()

player1_hands, player2_hands = split_hands(data)

hand_rankings = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

def high_card(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    return True, values_indices[-1]

def one_pair(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    for i in range(4):
        if values_indices[i] == values_indices[i+1]:
            return True, values_indices[i]
    return False, 0

def two_pair(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    pairs = []
    for i in range(4):
        if values_indices[i] == values_indices[i+1]:
            pairs.append(values_indices[i])
    if len(pairs) == 2:
        return True, max(pairs)
    return False, 0

def three_of_a_kind(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    for i in range(3):
        if values_indices[i] == values_indices[i+1] == values_indices[i+2]:
            return True, values_indices[i]
    return False, 0

def straight(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    if values_indices == [0, 1, 2, 3, 12]:
        return True, 3
    for i in range(4):
        if values_indices[i] + 1 != values_indices[i+1]:
            return False, 0
    return True, values_indices[-1]

def flush(hand):
    suits = [card[1] for card in hand]
    if len(set(suits)) == 1:
        return True, 0
    return False, 0

def full_house(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    if values_indices[0] == values_indices[1] and values_indices[2] == values_indices[3] == values_indices[4]:
        return True, values_indices[2]
    if values_indices[0] == values_indices[1] == values_indices[2] and values_indices[3] == values_indices[4]:
        return True, values_indices[0]
    return False, 0

def four_of_a_kind(hand):
    values = [card[0] for card in hand]
    values_indices = sorted("23456789TJQKA".index(value) for value in values)
    if values_indices[0] == values_indices[1] == values_indices[2] == values_indices[3]:
        return True, values_indices[0]
    if values_indices[1] == values_indices[2] == values_indices[3] == values_indices[4]:
        return True, values_indices[1]
    return False, 0

def straight_flush(hand):
    return straight(hand)[0] and flush(hand)[0], straight(hand)[1]

def royal_flush(hand):
    return straight_flush(hand)[0] and high_card(hand)[1] == 12, 0

def hand_rank(hand):
    overall_rank = 0
    if royal_flush(hand)[0]:
        if hand_rankings["Royal Flush"] > overall_rank:
            overall_rank = hand_rankings["Royal Flush"]
    elif straight_flush(hand)[0]:
        if hand_rankings["Straight Flush"] > overall_rank:
            overall_rank = hand_rankings["Straight Flush"]
    elif four_of_a_kind(hand)[0]:
        if hand_rankings["Four of a Kind"] > overall_rank:
            overall_rank = hand_rankings["Four of a Kind"]
    elif full_house(hand)[0]:
        if hand_rankings["Full House"] > overall_rank:
            overall_rank = hand_rankings["Full House"]
    elif flush(hand)[0]:
        if hand_rankings["Flush"] > overall_rank:
            overall_rank = hand_rankings["Flush"]
    elif straight(hand)[0]:
        if hand_rankings["Straight"] > overall_rank:
            overall_rank = hand_rankings["Straight"]
    elif three_of_a_kind(hand)[0]:
        if hand_rankings["Three of a Kind"] > overall_rank:
            overall_rank = hand_rankings["Three of a Kind"]
    elif two_pair(hand)[0]:
        if hand_rankings["Two Pair"] > overall_rank:
            overall_rank = hand_rankings["Two Pair"]
    elif one_pair(hand)[0]:
        if hand_rankings["One Pair"] > overall_rank:
            overall_rank = hand_rankings["One Pair"]
    elif high_card(hand)[0]:
        if hand_rankings["High Card"] > overall_rank:
            overall_rank = hand_rankings["High Card"]
    return overall_rank

testhand1 = ['5H', '5C', '6S', '7S', 'KD']

def compare_hands(hand1, hand2):
    if hand_rank(hand1) > hand_rank(hand2):
        return 1
    if hand_rank(hand1) == hand_rank(hand2) == 1:
        if high_card(hand1)[1] > high_card(hand2)[1]:
            return 1
        
    if hand_rank(hand1) == hand_rank(hand2) == 2:
        if one_pair(hand1)[1] > one_pair(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 3:
        if two_pair(hand1)[1] > two_pair(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 4:
        if three_of_a_kind(hand1)[1] > three_of_a_kind(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 5:
        if straight(hand1)[1] > straight(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 6:
        if flush(hand1)[1] > flush(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 7:
        if full_house(hand1)[1] > full_house(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 8:
        if four_of_a_kind(hand1)[1] > four_of_a_kind(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 9:
        if straight_flush(hand1)[1] > straight_flush(hand2)[1]:
            return 1
    if hand_rank(hand1) == hand_rank(hand2) == 10:
        return 0
    

player1_wins = 0
player2_wins = 0
for i in range(len(player1_hands)):
    result = compare_hands(player1_hands[i], player2_hands[i])
    if result == 1:
        player1_wins += 1

print(player1_wins)




