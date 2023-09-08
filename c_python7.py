### 1 ###
from learntools.python import jimmy_slots
graph = jimmy_slots.get_graph()
graph


def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph


q1.solution()


### 2 ###
def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        racer = racers[i]
        if racer['finish'] == 1:
            for i in racer['items']:
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts


sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
best_items(sample)


from learntools.python.luigi_analysis import full_dataset

def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        racer = racers[i]
        if racer['finish'] == 1:
            for i in racer['items']:
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

best_items(full_dataset)


### 3 ###
def hand_total(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)

    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)

q3.check()