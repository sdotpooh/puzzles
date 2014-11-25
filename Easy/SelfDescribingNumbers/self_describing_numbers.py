__author__ = "Sean Vinas."
__date__ = "23 November 2014"
__doc__ = "A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number."

from sys import argv


def self_describing(number):
    """ Verifies every digit is a self describing number.
    >>> self_describing([2, 0, 2, 0])
    1
    >>> self_describing([0])
    0
    """
    for i in range(len(number)):
        if number.count(i) != number[i]:
            return 0
    return 1


def main():
    """ Reads lines from text file and prints results if self describing."""
    textfile = open(argv[1], 'r')
    for line in textfile:
        number = [int(n) for n in line.rstrip('\n')]
        print(self_describing(number))
    textfile.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
