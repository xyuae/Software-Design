import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1"
    return h1-h2 == 1


def nextto(h1, h2):
    "Two houses are next to each otehr if they differ by 1"
    if h1-h2 == 1 or h2 - h1 == 1:
        return True
    else:
        return False

def zebra_puzzle():
    "Return a tuple (Water, Zebra) indicating their house numbers"
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, oj, WATER) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliament) in orderings
                if Englishman is red # 2
                if Spaniard is dog #3
                )

print zebra_puzzle()