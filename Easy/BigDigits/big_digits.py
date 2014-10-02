'''
Created on 2 Octber 2014
@author: Sean R. Vinas
@email:  vinassr@gmail.com
___________________________________
Copyright (c) 2014, Sean R. Vinas
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import fileinput
from sys import argv

class Digit(object):
    def __init__(self, value):
        self.value = value
        self.row_one = ''
        self.row_two = ''
        self.row_three = ''
        self.row_four = ''
        self.row_five = ''
        self.row_six = '-----'
        self.rows = {1:'*--*-', 2:'*----', 3:'-*---', 4:'--*--',
                     5:'---*-', 6:'-**--', 7:'-***-', 8:'***--',
                     9:'****-'}
        self.decode = {0:self.zero, 1:self.one, 2:self.two,
                       3:self.three, 4:self.four, 5:self.five,
                       6:self.six, 7:self.seven, 8:self.eight,
                       9:self.nine}
        try:
            self.decode[value]()
        except KeyError:
            ''' Redundant/extra protection.'''
            self.row_six = ''

    def zero(self):
        self.row_one  = self.rows[6]
        self.row_two  = self.rows[1]
        self.row_three= self.rows[1]
        self.row_four = self.rows[1]
        self.row_five = self.rows[6]
    def one(self):
        self.row_one  = self.rows[4]
        self.row_two  = self.rows[6]
        self.row_three= self.rows[4]
        self.row_four = self.rows[4]
        self.row_five = self.rows[7]
    def two(self):
        self.row_one  = self.rows[8]
        self.row_two  = self.rows[5]
        self.row_three= self.rows[6]
        self.row_four = self.rows[2]
        self.row_five = self.rows[9]
    def three(self):
        self.row_one  = self.rows[8]
        self.row_two  = self.rows[5]
        self.row_three= self.rows[6]
        self.row_four = self.rows[5]
        self.row_five = self.rows[8]
    def four(self):
        self.row_one  = self.rows[3]
        self.row_two  = self.rows[1]
        self.row_three= self.rows[9]
        self.row_four = self.rows[5]
        self.row_five = self.rows[5]
    def five(self):
        self.row_one  = self.rows[9]
        self.row_two  = self.rows[2]
        self.row_three= self.rows[8]
        self.row_four = self.rows[5]
        self.row_five = self.rows[8]
    def six(self):
        self.row_one  = self.rows[6]
        self.row_two  = self.rows[2]
        self.row_three= self.rows[8]
        self.row_four = self.rows[1]
        self.row_five = self.rows[6]
    def seven(self):
        self.row_one  = self.rows[9]
        self.row_two  = self.rows[5]
        self.row_three= self.rows[4]
        self.row_four = self.rows[3]
        self.row_five = self.rows[3]
    def eight(self):
        self.row_one  = self.rows[6]
        self.row_two  = self.rows[1]
        self.row_three= self.rows[6]
        self.row_four = self.rows[1]
        self.row_five = self.rows[6]
    def nine(self):
        self.row_one  = self.rows[6]
        self.row_two  = self.rows[1]
        self.row_three= self.rows[7]
        self.row_four = self.rows[5]
        self.row_five = self.rows[6]

class Lines(object):
    def __init__(self, small_digits):
        self.line1 = ''
        self.line2 = ''
        self.line3 = ''
        self.line4 = ''
        self.line5 = ''
        self.line6 = ''
        self.small_digits = small_digits
        self.convert_to_big()
    def convert_to_big(self):
        for digit in self.small_digits:
            digit = Digit(digit)
            self.line1 += digit.row_one
            self.line2 += digit.row_two
            self.line3 += digit.row_three
            self.line4 += digit.row_four
            self.line5 += digit.row_five
            self.line6 += digit.row_six
    def print_lines(self):
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.line6)

class Big_Digits(object):
    def __init__(self, filename):
        self.filename = filename
        self.read_file()
        #self.each_line = []
    def read_file(self):
        for line in fileinput.input(self.filename):
            line = line.rstrip('\n')
            l = []
            for c in line:
                try:
                    l.append(int(c))
                except ValueError:
                    pass
            #self.each_line.append(Lines(l))
            Lines(l).print_lines()
            #del ls[:]



def main():
    bd = Big_Digits(argv[1])



if __name__ == '__main__':
    main()
