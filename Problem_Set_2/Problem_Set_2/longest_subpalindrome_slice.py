def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text"
    n = len(text)
    maxLen = 0
    head = 0;
    tail = 0;
    for i in range(n+1):
        for j in range(i+1, n+1):
            if j - i <= maxLen: pass
            elif is_palindrome(text[i:j]):
                head, tail = i, j
                maxLen = j - i
    return head, tail

def is_palindrome(subtext):
    "Return true if subtext is a palindrome and otherwise return false"
    n = len(subtext)
    if n == 0: return False
    if n == 1: return True

    head, tail = 0, n - 1
    while head < tail:
        if subtext[head].lower() != subtext[tail].lower():
            return False
        head += 1
        tail -= 1
    return True


def test2():
    I = is_palindrome
    assert I('racecar') == True
    assert I('Racecar') == True
    assert I('IamaCar') == False
    print("Success")


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

#test2()
test()
