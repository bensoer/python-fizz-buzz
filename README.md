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
python3 ./fizzbuss.py 85
```

# What is FizzBuzz ?
FizzBuzz is a math game often taught to children to practice their multiplication. The game is played between two people each counting
up from one until a target number. Each person takes turn saying the number, unless the number is divisible by 3 or 5. If the value
is divisible by 3, the player is to say "Fizz!" rather then the number. If the value is divisible by 5, the player is to say "Buzz". If
the value is divisible by both, the player is to say "FizzBuzz!". The winner is determined when one of the two players messes up, 
making the other player the winner

This game has been popularised also as a programming technical question as it showcases a developers coding styles and preferences in
solving problems and organising their code. One of the big determining factors, is whether the developer is someone who codes more for
producing a result, or for developing a reusable solution

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
effectively modify or add on to the application without causing more chaos in the legibility and introducing more bugs into the existing
code. The only time I believe these highly optimised and clever implementations are valuable is when speed and performance is the utmost 
importance in the development of the application. Additionally, software development is most often an iterative process and refactoring
for performance is often a much easier task, then refactoring for legibility and reusability.

**Note:** I read up on a heavily performant implementation of solving fizzbuzz. You can see it in `fizzbuzz_fast.py`. To my case and point, it took
me a good 10-15 minutes of researching and adding `print()` statements to understand how this did what it did. I'm not a fan of it due to how
quickly the code has become unlegible and requiring more niche python knowledge to the performance increase that doesn't really matter. I have
added commenting to the code to explain how it works.

