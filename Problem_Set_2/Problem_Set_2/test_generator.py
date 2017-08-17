import time


def sq(x):
    print 'sq called', x;
    return x * x

g = (sq(x) for x in range(10) if x%2 == 0)

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result"
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def timedcalls(n, fn, *args):
    "Call function n times with args; return the min, avg, and max time."
    "Call fn(*args) repeatedl: n times if n is an int, or up to n seconds if n is a float; return the min, avg, and max time."
    if isinstance(n,int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args))
    return min(times), average(times), max(times)

def average(numbers):
    "Retrn the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1


def all_ints(start = 0 , end = None):
    "Generate integers in the order 0, +1, -1, "
    yield 0
    for i in ints(1):
        yield +i
        yield -i

