'''
Created on 25 September 2014
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

class Digits(object):
    def __init__(self, digit):
        self.digit = digit
        self.digit_sum = 0
        self.sum_digit()
    def sum_digit(self):
        if (self.digit == '0'):
            pass
        else:
            for c in self.digit:
                self.digit_sum += int(c)


class Sum_Of_Digits(object):
    def __init__(self, filename):
        self.filename = filename
        self.digits = []
        self.read_file()
        self.print_sum()
    def read_file(self):
        for line in fileinput.input([self.filename]):
            self.append_digit(line.rstrip('\n'))
    def append_digit(self, digit):
        self.digits.append(Digits(digit))
    def print_sum(self):
        for d in self.digits:
            print (d.digit_sum)


def main():
    Sum_Of_Digits(argv[1])


if __name__ == '__main__':
    main()
