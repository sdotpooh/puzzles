__author__ = "Sean R. Vinas"
__date__ = "21 November 2014"
__doc__ = "Unshuffle words in a text."


from sys import argv


def line_to_list_of_2lists(line):
    """ Convert's a text line to a list of two lists i.e.
    >>> line_to_list_of_2lists('programming first The language;3 2 1')
    [['programming', 'first', 'The', 'language'], [3, 2, 1]]
    """
    divide_line = line.rstrip('\n').split(';')
    sentence = divide_line[0].split()
    decoder_index = list(map(int, divide_line[1].split()))
    list_of_2list = [sentence, decoder_index]
    return list_of_2list


def decoder(line):
    """ Decode based on index and print results.
    >>> decoder([['programming', 'first', 'The', 'language'], [3, 2, 1]])
    The first programming language \n
    """
    for i in range(1, len(line[1])+2):
        try:
            loc = line[1].index(i)
            print(line[0][loc], sep=' ', end = ' ')
        except ValueError:
            print(line[0][-1], sep=' ', end = ' ')
    print()


def main():
    f = open(argv[1], 'r')
    for line in f:
        decoder(line_to_list_of_2lists(line))
    f.close()



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
