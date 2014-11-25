'''Sean Vinas 19 Nov 2014'''

from sys import argv
import unittest


def format_input(line):
    '''line will either be blank, \n, or (x0, y0) (x1, y1) where
    x0, x1, y0, and y1 are signed integers.
    return as [x0, y0, x1, y1]'''
    temp_line = ''
    for c in line:
        if c == ' ' or c == '-' or c.isdigit():
            temp_line += c
    format_line = temp_line.split()
    formatted_line = list(map(int, format_line))
    return formatted_line


def distance(coor_list):
    ''' return sqrt((x1-x0)^2 + (y1-y0)^2)'''
    x_diff_squared = (coor_list[2]-coor_list[0])**2
    y_diff_squared = (coor_list[3]-coor_list[1])**2
    return int((x_diff_squared + y_diff_squared)**(1/2))


class Test_format_input_function(unittest.TestCase):

    def test_format_input_zeros(self):
        line = '(0, 0) (0, 0)'
        self.assertEqual(format_input(line), [0, 0, 0, 0])

    def test_format_input_neg_zeros(self):
        line = '(-0, -0) (-0, -0)'
        self.assertEqual(format_input(line), [0, 0, 0, 0])


class Test_distance_function(unittest.TestCase):

    def test_distance_zeros(self):
        line = [0, 0, 0, 0]
        self.assertEqual(distance(line), 0)

    def test_distance_ones(self):
        line = [1, 1, 1, 1]
        self.assertEqual(distance(line), 0)



def main():
    text_file = open(argv[1], 'r')
    for line in text_file:
        line = format_input(line)
        print(distance(line))


if __name__=='__main__':
    if len(argv) > 1:
        main()
    else:
        unittest.main()
