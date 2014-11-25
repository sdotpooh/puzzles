__author__ = "sean R. Vinas."
__date__ = "23 November 2014."
__doc__ = "An Armstrong number is an n-digit number that is equal to the sum of the n'th powers of its digits. Determine if the input numbers are Armstrong numbers."


from sys import argv


def armstrong(numbers, number):
    """ Sum of the n'th powers of it's digits.
    >>> armstrong([6], 6)
    True
    """
    n = len(numbers)
    cumsum = 0
    for i in numbers:
        cumsum += i**n
    if number == cumsum:
        return True
    else:
        return False

def main():
    """ Read each line in the text file and verify if Armstrong number."""
    textfile = open(argv[1], 'r')
    for line in textfile:
        number = line.rstrip('\n')
        numbers = [int(n) for n in number]
        print(armstrong(numbers, int(number)))
    textfile.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
