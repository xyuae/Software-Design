# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    "Return a list of n random hands: deal(numhands, n, deck) = [hand, ...]"
    if numhands * 5 > 52:
        print("Card drawn out")
        return None
    random.shuffle(deck)
    return [deck[n * i: n * i + n] for i in range(numhands)]

def test():
    "Test the deal() function, return a list of hands"
    return deal(3)

if __name__ == '__main__':
    print(test())



