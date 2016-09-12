import random
import sys


def gen_random_number():
    while 1 is not 0:
        yield random.randint(1, sys.maxint)


if __name__ == '__main__':
    gen_random_number()