def longest_local_subpalindrome(text, index1, index2, n):
    """Return (i, j) of the longest palindrome centered by [index1, index2], n is the length of string text"""
    l1 = index1
    r1 = index2
    while l1 >=0 and r1 < n:
        if text[l1].lower() == text[r1].lower():
            l1 -= 1
            r1 += 1
        else: break
    return l1 +1 , r1



def test():
    L = longest_subpalindrome_slice
    print(L('racecar'))
    print(L('Race car'))
    assert L('racecar') == L('Racecar') == (0, 7) == L('RAcecarX')
    assert L('Race car') == (0, 1)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    print("Success")



def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text"
    n = len(text)
    if n == 0: return 0, 0
    left, right = 0, 1
    maxLen = right - left
    for i in range(1, n):
        l, r = longest_local_subpalindrome(text, i-1, i, n)
        if r - l > maxLen: left, right, maxLen = l, r, r - l
        l, r = longest_local_subpalindrome(text, i-1, i+1, n)
        if r - l > maxLen: left, right, maxLen = l, r, r - l
    return left, right

test()
