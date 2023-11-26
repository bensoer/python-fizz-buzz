# Implementation from: https://builtin.com/software-engineering-perspectives/fizzbuzz-python
# Itertools resources:
# - https://www.geeksforgeeks.org/python-itertools-cycle/

import itertools

def fizz_buzz(x):

    # This creates infinite iterators. 'fizzes' is an infinite iterator will put the word 'Fizz' at every 3rd index, and empty string at the rest
    # 'buzzes' is an infinite iterator that will put the word 'Buzz' at every 5th index, and empty string at the rest
    # Effectively this is counting along and putting Fizz and Buzz every third and fifth, because we know every third value will divide by 3, 
    # and every fifth will divide by 5 
    fizzes = itertools.cycle([''] * 2 + ["Fizz"])
    buzzes = itertools.cycle([''] * 4 + ["Buzz"])

    # Then create an iterator fizzes_buzzes that iterates through each of the above iterators at the same positions in each and merges their strings
    # together, creating either empty strings or strings containing Fizz, Buzz or FizzBuss
    # See how zip() works: https://www.w3schools.com/python/ref_func_zip.asp
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))

    # Then loop through fizzes_buzzes with a number value (itertools.count(1) infinitly counts up in increments of its 
    # parameter value) and check whether `word` has a value or is an empty string. If it is empty this will evaluate 
    # as false and the "or" will then use 'n' which is the index position
    # This is all merged also into an iterator 'result'
    result = (word or n for word, n in zip(fizzes_buzzes, itertools.count(1)))

    # Finally, iterate through the result iterator but only up to index 'x'
    # print every value you are given
    for i in itertools.islice(result, x):
        print(i)


# Play FizzBuzz up to 100
fizz_buzz(100)