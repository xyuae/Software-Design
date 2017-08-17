

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+ 10*0 + 100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'
    """
    result = ''
    stack = []
    count = 0
    word += ' '
    for element in word:
        if element.isupper():
            stack.append(element)
            count =count + 1
        else:
            if len(stack) != 0:
                tempCount = 0
                res = '('
                res += str(10**tempCount) + '*' + stack.pop()
                tempCount += 1
                while len(stack) != 0:
                    res += '+' + str(10**tempCount) + '*' + stack.pop()
                    tempCount += 1
                res += ')'
                result += res
            result = result + element
    result.strip()
    return result


def compile_word2(word):
    print word[::-1]
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word
