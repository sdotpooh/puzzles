from sys import argv

__author__ = "Sean R. Vinas"
__date__ = "20 November 2014"
__doc__ = """Finds the lowest unique number in a list.
Codeeval.com challenge 103.
"""


def dict_insert(key, picks):
    """ If key is not in picks add it, else increment value."""
    if key in picks:
        picks[key] += 1
    else:
        picks[key] = 1


def unique(picks, line):
    """
    Returns the index (starting from 1) of the item in the line who is unique,
    one occurence, and if multiple, returns the min item.
    >>> unique({'1':1, '2':1}, ['1', '2'])
    1
    >>> unique({'3':2, '6':1, '9':1, '-8':1}, ['3','3','9','6','-8'])
    5
    >>> unique({'3':2, '4':2}, ['3','3','4','4'])
    0
    """
    unique_list = filter(lambda x: x[1] == 1, picks.items())
    unique_sorted = sorted([int(i[0]) for i in unique_list])
    if len(unique_sorted) > 0:
        unique_key = line.index(str(unique_sorted[0]))
        return (unique_key+1)
    else:
        return 0


def main():
    """ Main function. Reads file input.txt each line contains a list, find unique index."""
    picks = dict()
    input_file = open(argv[1], 'r')
    for line in input_file:
        line = line.rstrip('\n').split()
        for i in line:
            dict_insert(i, picks)
        print(unique(picks, line))
        picks.clear()
    input_file.close()


if __name__=='__main__':
    import doctest
    doctest.testmod()
    main()
