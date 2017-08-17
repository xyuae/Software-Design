from collections import defaultdict
from math import factorial
from random import randrange
from shuffle import shuffle, swap


def test_shuffler(shuffler, deck='abcd', n=100000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))
    ok = all((0.9 <= counts[item]/e <= 1.1)
             for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
    print '   ',
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" % (item, count*100./n),
    print


def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)


def shuffle1(deck):
    "Another way of shuffle"
    N = len(deck)
    for i in range(N):
        swap(deck, i, randrange(N))


def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc', 'ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

if __name__ == '__main__':
    test_shufflers()
