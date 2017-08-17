import itertools


def lives(a, b):
    return a == b

def adjacent(a, b):
    return abs(a-b) < 2

def higher(a, b):
    return a > b


def Floor_Puzzle():
    floors =bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = itertools.permutations(floors)
    return next ((Hopper, Kay, Liskov, Peris, Ritchie) for (Hopper, Kay, Liskov, Peris, Ritchie) in orderings
                 if not lives(Hopper, top) #1
                 if not lives(Kay, bottom) #2
                 if not lives(Liskov, top) and not lives(Liskov, bottom) #3
                 if higher(Peris, Kay)   #4
                 if not adjacent(Ritchie, Liskov) #5
                 if not adjacent(Liskov, Kay) # 6
                 )


print Floor_Puzzle()