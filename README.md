# Python Fizz Buzz
Python Fizz Buzz is an implementation of the Fizz Buzz game, implemented in python as a CLI script

# Prerequisites
- Python 3.9.2+

# Quickstart
1. Clone the repository
2. Execute the `fizzbuzz.py` as follows:
    ```bash
    python3 ./fizzbuzz.py 100
    ```
# Usage
To see all help options run the following command:
```bash
python3 ./fizzbuzz.py -h
```
# Options
| Parameter | Default Value | Description |
| --------- | ------------- | ----------- |
| `count`   | 100           | How high to play FizzBuzz up to |
| `-h`      | N/A           | Print out the help screen |

Example Usage:
```bash
# Automatically play FizzBuzz to 100
python3 ./fizzbuzz.py

# Play FizzBuss up to 85
python3 ./fizzbuzz.py 85
```

# What is FizzBuzz ?
FizzBuzz is a math game often taught to children to practice their multiplication. The game is played between two people each counting
up from one until a target number. Each person takes turn saying the number, unless the number is divisible by 3 or 5. If the value
is divisible by 3, the player is to say "Fizz!" rather then the number. If the value is divisible by 5, the player is to say "Buzz". If
the value is divisible by both, the player is to say "FizzBuzz!". The winner is determined when one of the two players messes up, 
making the other player the winner

This game has been popularised also as a programming technical question as it showcases a developers coding styles and preferences in
solving problems and organising their code. One of the big factors, this question often showcases is whether the developer favors coding to produce a result, to be performant, or for high reusability. Depending on the hiring team needs, asking this question can be very insightful in whether the potential candidate aligns with the teams values.

**References**
* https://www.youtube.com/watch?v=QPZ0pIK_wsc&t=130s
* https://builtin.com/software-engineering-perspectives/fizzbuzz
* https://builtin.com/software-engineering-perspectives/fizzbuzz-python


## So what is this implementation ?
My implementation of FizzBuzz leans heavily towards reusability and breaking apart much of the problem into multiple functions to enforce
modularity, legibility and reusability. This problem is not one that demands performance in the code and overall is not a resource intensive
application to operate, so legibility to figure out what is going on and the scalability for the program to be easily modified and expanded
on by a developer is my preferred priority in the development. My preference, is that code should be highly legible and organised. Highly
optimised and clever implementations exist, but these always come at the expense of requiring a more skilled developer to understand and
effectively modify or add on to the application without causing more chaos in the legibility and/or introducing more bugs into the existing
code. The only time I believe these highly optimised and clever implementations are valuable is when speed and performance is the utmost 
importance in the development of the application. 

As an additional point, software development is most often an iterative process and refactoring for performance is often a much easier task, then refactoring for legibility and reusability.

### An Argument Against A Performant FizzBuzz
I read up on a heavily performant implementation of solving fizzbuzz. You can see it in `fizzbuzz_fast.py`. To my case and point, it took
me a good 10-15 minutes of researching and adding `print()` statements to understand how this did what it did. I'm not a fan of it due to how
quickly the code has become unlegible and requiring more niche python knowledge to the performance increase that doesn't really matter. I have
added commenting to the code to explain how it works if you are interested, and so that I don't forget if I stumble upon this in the future.

I favor my implementation, because although `fizzbuzz_fast.py`'s implementation is faster, `fizzbuzz.py`'s implementation is much easier 
to expand and extend. Say we want to expand the game now to Fizz Buzz Bang!. Where 'Bang!' is for numbers that divide nicely by 7. We can 
easily do this by implementing as follows:
```python
def is_bang(number: int) -> bool:
    return is_divisible_by(number, 7)
```
and then add it as an additional condition in the loop:
```python
for i in range(1, count_to+1):
    # ...

    if is_bang(i):
        output += "Bang"
    
    # ...
```

We could even evolve the game in a new direction to include 'Prime!'. This can be easily done by implemented as:
```python
def is_prime(number: int) -> bool:

    # prime numbers must be positive numbers and 1 is not a prime
    if number < 2:
        return False
    
    for i in range(2, number):
        if is_divisible_by(number, i):
            return False
    return True
```
And then again, added as an additional condition in the loop

