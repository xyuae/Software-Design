"""
Python supports the creation of anonymous function
Using a construct called "lambda". 
It is often used in conjuction with typical functional
concepts like filter(), map() and reduce()
"""
def f(x): return x**2

print f(8)

g = lambda x: x**2
print g(8)
"""
doc: You can put a lambda definition anywhere a function is expected, and you don't 
have to assign it to a variable at all
"""
def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)

print f(42), g(42)

print make_incrementor(22)(33)
"""
doc: You can now create multiple different incrementor funcitons and assign them to 
vairables, then use them independent from each other. As the last
statement demonstrates, you don't even have to assign the funciton anywhere -- you can just use it 
instantly and forget it when it's not needed anymore
"""

foo = [2, 18, 9, 22, 17]    
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)
"""
doc: First we define a simple list of integer values, then we use
the standard functions filter(), map and reduce() to do various things with taht list. 
All of the three functions expect two arguments: A function and a list.
We could define a separate function somewhere else and then use that function's name
as an argument to filter() etc., and in fact that's probably a good idea if we're going to use that function 
several times, or if the function is too complex for writing in a single line. However, if we need it only once and it's 
quite simple, it's more convenient to use a lambda construct to generate a anonymous funciton and pass it to filter() imeediately.
this creates very companct, yet readable code
reduce() is somewhat special. The "worker function" for this one must accept two 
arguments, not just one. The funciton is called with the first two elements
from the list, then with the result of that call and the thrid element, and so on, until
all of the list elements have been handled. This means that our funciton is called n-1 times if the list contains n elements.
The return value of the last call is the result of the reduce() construct. in the above example, itsimply adds the rguments, so we get the sum of all elements.
"""
    
"""
doc: The following example is one way to compute prime numbers in Python
"""    
nums = range(2, 50)
for i in range(2, 8):
    nums = filter(lambda x: x == i or x % i, nums)
    
    print nums
"""
doc: First, we put all numbers from 2 to 49 into a list called nums
Then we have a for loop that iterates over all possible divisors, i.e. the value of i goes from 2 to 7. Naturally, all nubers that are multiples of those divisors cannot 
be prime numbers, so we use a filter funciton to remove them prom the list. The algorihtm is called the sieve of Eratosthenes
In the above case, the filter funciton simply syas: "Leave the element in the list if it is equal to i, or if it leaves a non-zero remainder when divided by i.
Otherwise remove it from the list." After the filtering loop finishes, only prime numbers are left,
of course. I am not aware of a languge in which you can do the same thing with built-in features
as compact and as readable as in Python.
"""
sentence = 'It is raining cats and dogs'
words = sentence.split()
print words
lengths = map(lambda word: len(word), words)
print lengths

"""
doc: The getoutput functioin from the commands module (which is part of the Python standard library) runs the given
command and returns its output as a single string. Therefore, we split it up into separate lines first. Finally we use map with a 
lambda funciton that splits each line and returns just the third element of the result, which is the mountpoint.
When writing "real-word" scripts, it is recommended to split up complex statements
so that it is easier to see what it does. Also, it si easier to make changes
Howver, the task of splitting up the output of a commnad into a list of line is very common.
You need it all the time when parsing the output of external commands. Therefore, it is common practice to 
include the split operation on the getoutput line. But do the rest separately. 
"""
lines = commands.getoutput('mount -v').splitlines()
points = map(lambda line: line.split()[2].lines)

"""
doc: On a related note, you can also use so-called list comprehensions to construct lists from other lists. Sometimes this is preferable because of efficiency or 
readability. The previous exmaple could very well be rewritten using a list comprehension:
"""
lines = commands.getoutput('mount -v').splitlines()
points = [line.split()[2] for line in lines]
print points

