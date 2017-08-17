

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    for i in range(len(ranks) -1):
        if ranks[i] != ranks[i + 1] + 1:
            return False
    return True

def flush(hand):
    "Return True if all the cards have the same suit."
    suit = [s for r,s in hand]
    for i in range(len(hand) - 1):
        if suit[i] != suit[i + 1]:
            return False
    return True

def test2():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'
    
print(test2())


# -----------
# User Instructions
# 
# Define a function, kind(n, ranks).

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    nums = {}
    for r in ranks:
        if r in nums:
            nums[r] = nums[r] + 1
        else:
            nums[r] = 1
    for k,v in nums.iteritems():
        if v == n:
            return k
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    for r in ranks:
        if ranks.count(r) == 2:
            lower = r
    for r in list(reversed(ranks)):
        if ranks.count(r) == 2:
            higher = r
    if higher != lower:
        return higher, lower
    return None
    

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    alphabet = 'TJQKA'
    change = [10, 11, 12, 13, 14]
    for r,s in cards:
        if alphabet.find(r) != -1:
            r = change[alphabet.find(r)]
    ranks = [r for r,s in cards]
    ranks.sort(reverse=True)
    if len(set(ranks)) == 5 and ranks[-1] == 2:
        return [5, 4, 3, 2, 1]
    return ranks
    # return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


print(card_ranks(['AC', '3D', '4S', 'KH']))  # should output [14, 13, 4, 3]
