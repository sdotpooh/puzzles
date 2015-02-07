"""
Write a program which determines the Mth to the last element in a list.
https://www.codeeval.com/open_challenges/10/
"""

__author__ = 'seanvinas'
__date__ = "30 January 2015"


def main():
    with open('input.txt', 'r') as f:
        lines = (lines.rstrip('\n').split() for lines in f)
        for line in lines:
            location = int(line.pop(-1))
            word_len = len(line)
            if word_len >= location:
                print(line.pop(word_len-location))


if __name__ == '__main__':
    main()