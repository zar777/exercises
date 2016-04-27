import sys


def calc(x):
    return x * 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Not enough arguments')
    print calc(int(sys.argv[1]))