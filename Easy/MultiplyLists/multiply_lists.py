'''Sean Vinas 19 Nov 2014'''
from sys import argv


def list_multiply(list_a, list_b):
    '''
    Input 2 lists, multiply the contents & return a list
    For example:
    >>> list_multiply([0], [0])
    [0]

    >>> list_multiply([9, 0, 6], [15, 14, 9])
    [135, 0, 54]

    >>> list_multiply([5], [8])
    [40]

    >>> list_multiply([13, 4, 15, 1, 15, 5] , [1, 4,15, 14, 8, 2])
    [13, 16, 225, 14, 120, 10]
    '''
    return [a*b for a,b in zip(list_a,list_b)]


def line_to_2lists(line):
    '''
    Converts a string input to be converted to two lists based on | as shown:
    >>> line_to_2lists('0 0 | 0 1')
    [[0, 0], [0, 1]]

    >>> line_to_2lists('0 0 0 | 0 0 1')
    [[0, 0, 0], [0, 0, 1]]
    '''
    line_split = line.rstrip('\n').split('|')
    list_a = list(map(int, line_split[0].split()))
    list_b = list(map(int, line_split[1].split()))
    return [list_a, list_b]


def main():
    f = open(argv[1], 'r')
    for line in f:
        lists = line_to_2lists(line)
        print(*list_multiply(lists[0], lists[1]))
    f.close()


if __name__=='__main__':
    if len(argv) > 1:
        main()
    else:
        import doctest
        doctest.testmod()
