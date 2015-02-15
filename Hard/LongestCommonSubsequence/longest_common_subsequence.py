__author__ = 'seanvinas'
__date__ = '6 February 2015'
"""Find the longest common subsequence between two strings."""
from functools import lru_cache


@lru_cache(maxsize=None)
def lcs(first_word, second_word):
    if not first_word or not second_word:
        return ""
    first_word_first_letter = first_word[0]
    first_word_remaining = first_word[1:]
    second_word_first_letter = second_word[0]
    second_word_remaining = second_word[1:]

    if first_word_first_letter == second_word_first_letter:
        return first_word_first_letter + lcs(first_word_remaining,
                                             second_word_remaining)
    else:
        return max(lcs(first_word, second_word_remaining),
                   lcs(first_word_remaining, second_word),
                   key=len)


def main():
    with open('input.txt', 'r') as f:
        lines = (line.rstrip('\n') for line in f)
        for line in lines:
            word_a, word_b = line.split(';')
            common = lcs(word_a, word_b)
            print(common)


if __name__ == '__main__':
    main()