import re

import itertools
import string

from compile_word import *



def compile_formula(formula, verbose = False):
    """Compile formula into a function. Also returns letters found, as a str,
    in same order as parms of function. For example, 'YOU = ME ** 2' :returns
    (lambda Y, M, E, U, O: (U + 10 * 0 + 100 * Y) == (E + 10 * M)***2, 'YMEUO"""

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ','.join(letters)
    body = compile_word(formula)
    # print body
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters

def valid(f):
    "Formula f is valid iff it has no numbers with leading zero, and evals true."
    try:
        return not re.search(r'\b0[0-9]', f)
    except ArithmeticError:
        return False

def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filed-in string or None.
    This version precompiles the formula; only one eval per formula"""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters,''.join(map(str, digits)))
                if valid(formula.translate(table)):
                    return formula.translate(table)
        except ArithmeticError:
            pass


print faster_solve("ODD + ODD == EVEN")