import random

def shuffle(list):
    "Return a randomly shuffled list"
    length = len(list)
    for i in range(length - 1):
        swap(list, i, random.randrange(i, length))

def swap(list, i, j):
    "Swap the ith and jth element in the list"
    list[i], list[j] = list[j], list[i]

def test():
    input = list('12345')
    shuffle(input)
    return input

if __name__ == '__main__':
    print test()
