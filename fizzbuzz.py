import argparse

def is_divisible_by(number: int, divisor: int)-> bool:
    '''
    Determines whether the passed in "number" divides evenly by the passed in "divisor" by using
    modulus division. If there is no remainder, then it divides evenly

    @return bool - TRUE means the "number" is divisible by the "divisor"
    '''
    return number % divisor == 0

def is_fizz(number: int) -> bool:
    '''
    Determines whether the number is a 'Fizz' number. By the rules of FizzBuzz. A 'Fizz' number
    is one that is divisible by 3

    @return bool - TRUE means the "number" is divisible by 3
    '''
    return is_divisible_by(number, 3)

def is_buzz(number: int) -> bool:
    '''
    Determines whetehr the number is a 'Buzz' number. By the rules of FizzBuzz, A 'Buzz' number
    is one that is divisible by 5

    @return bool - TRUE means the "number" is divisible by 5
    '''
    return is_divisible_by(number, 5)

def main():

    # Parse out arguments from the console
    parser = argparse.ArgumentParser(
            description='FizzBuzz Counting Application',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    parser.add_argument('count', help='How high to play FizzBuzz up to', default=100, type=int, nargs='?')

    args = parser.parse_args()
    count_to = args.count

    # Count up numbers, sorting numbers, Fizzes, Buzzes and FizzBuzzes
    for i in range(1, count_to+1):

        output = ""

        if is_fizz(i):
            output += "Fizz"

        if is_buzz(i):
            output += "Buzz"

        if len(output) == 0:
            output = "{}".format(i)

        print(output)



if __name__ == '__main__':
    main()