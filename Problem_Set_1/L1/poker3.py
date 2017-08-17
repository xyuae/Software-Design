import itertools


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable"
    result, maxvalue = [], None
    key = key or (lambda x: x)
    for item in iterable:
        if (key(item) > maxvalue):
            result, maxvalue = [item], key(item)
        elif key(item) == maxvalue:
            result.append(item)
    return result


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    hands = itertools.permutations(hand, 5)
    return max(hands, key=hand_rank)

def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first"
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(groups):
    return zip(*groups)


def hand_rank(hand):
    "Return a value indicating how high the hand ranks"
    # counts is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 2, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0), ranks
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "6C 7C 1C 2C 3C".split() # Flush
    st = "6C 7D 8C 9C TC".split() # Straight

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    return 'tests pass'

print(test())
