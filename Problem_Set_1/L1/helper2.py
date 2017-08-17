
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return True if all the cards have the same suit."
    suit = [s for r,s in hand]
    return len(set(suit)) == 1

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    nums = {}
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """ If there are two pair, return the two ranks as a 
    tuple: (highest, lowest); otherwise return None
    """
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks)[0], two_pair(ranks)[1], ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)        

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair([9, 9, 8, 8, 3]) == (9, 8)
    # print type(kind(4, fkranks))
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]
    return 'tests pass'


print(test())


def test2():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fl = "6C 7C 5C 2C 3C".split() # Flush
    st = "6C 7D 8C 9C TC".split() #
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8 , 7, 6]
    threeKind = "6C 6D 6H 3H 2H".split() # 3 of a kind
    assert hand_rank(threeKind) == (3, 6, [6, 6, 6,3,2])
    twoPair = "6C 6D 3H 3H 2H".split() # 2 of a kind
    # print twoPair
    assert hand_rank(twoPair) == (2, 6, 3, [6, 6, 3, 3, 2])
    kind = "6C 6D 2H 3H 4H".split() # 1 of a kind
    assert hand_rank(kind) == (1, 6, [6, 6, 4, 3, 2])
    nt = "6C 7D 2H 3H 4H".split()
    # print hand_rank(nt)
    assert hand_rank(nt) == (0, [7, 6, 4, 3, 2])
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(fl) == (5, [7, 6, 5, 3, 2])
    assert hand_rank(st) == (4, 10)
    return 'tests pass'


print(test2())
