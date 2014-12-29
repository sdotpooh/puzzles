__author__ = "Sean R. Vinas"
__date__ = "29 December 2014"
__doc__ = """ Find the number of steps in the shortest way from the entrance
on the first floor to the exit on the last floor, including entrance and exit.
Moving between levels is one step."""


from sys import argv


class Board(object):
    """A board is composed of N Floor levels of each NxN"""
    def __init__(self):
        """
        """
    def eliminate_inefficient_paths(self):
        """
        """



class Floor(object):
    """Each floor is NxN and contains an entrance, or a slot."""
    def __init__(self):
        """
        """
    def eliminate_inefficient_paths(self):
        """
        """



def main():
    filename = open(argv[1], 'r')
    for line in filename:
        print(line)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
