__author__ = "Sean R. Vinas."
__date__ = "23 November 2014"
__doc__ = "Modulo of two numbers, not including 0."

from sys import argv

def n_mod_m(n_m_list):
    """n mod m without using % operator.
    >>> n_mod_m([20, 6])
    2
    >>> n_mod_m([2, 3])
    2
    """
    while n_m_list[0] >= n_m_list[1]:
        n_m_list[0] -= n_m_list[1]
    return n_m_list[0]


def main():
    text_file = open(argv[1], 'r')
    for line in text_file:
        n_m_list = list(map(int, line.rstrip('\n').split(',')))
        print(n_mod_m(n_m_list))
    text_file.close()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
