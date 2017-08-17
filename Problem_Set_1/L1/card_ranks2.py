def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    alphabet = 'TJQKA'
    change = [10, 11, 12, 13, 14]
    ranks = []
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks
    
print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]