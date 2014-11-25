__author__ = "Sean R. Vinas."
__date__ = "23 November 2014."
__doc__ = "Given a string s, define the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example)."

from sys import argv
import string


def char_count(string_list):
    """Transform string list to a count of each letter in sorted order.
    >>> char_count(['a', 'b', 'b', 'c', 'c', 'c'])
    [3, 2, 1]"""
    count_list = []
    i = 0
    while i < len(string_list):
        n = string_list.count(string_list[i])
        count_list.append(n)
        i += n
    return sorted(count_list, reverse = True)


def calculate_beauty(count_list):
    """ Multiply the first item in the list by 26,
    the second item by 25, the third by 24...
    >>> calculate_beauty([3, 2, 1])
    152
    """
    n = 0
    cum_sum = 0
    for i in range(26, 26-len(count_list), -1):
        cum_sum += count_list[n]*i
        n += 1
    return cum_sum


def main():
    """ Open and read each line of the text file and calculate the beauty of
    each line."""
    letters = string.ascii_lowercase
    text_file = open(argv[1], 'r')
    for line in text_file:
        string_list = [n for n in line.rstrip('\n').lower() if n in letters]
        sorted_string = sorted(string_list)
        print(calculate_beauty(char_count(sorted_string)))
    text_file.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
