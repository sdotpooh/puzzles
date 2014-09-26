'''
Created on 23 September 2014
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

class Dec_To_Binary(object):
    def __init__(self, decimal, position_one, position_two):
        self.position_one = int(position_one)
        self.position_two = int(position_two)
        self.pos_one_value = 0
        self.pos_two_value = 0
        self.decimal = int(decimal)
        self.equality = 'false'
        self.dec2bin()
    def dec2bin(self):
        if (self.position_one <= 0) or (self.position_two <= 0):
            pass
        elif self.decimal < 0:
            pass
        else:
            self.pos_one_value = ((self.decimal >> self.position_one - 1) & 0x1)
            self.pos_two_value = ((self.decimal >> self.position_two - 1) & 0x1)
            if self.pos_one_value == self.pos_two_value:
                self.equality = 'true'


class Bit_Positions(object):
    def __init__(self, filename):
        self.filename = filename
        self.numbers = []
        self.read_file()
        self.print_equality()
    def read_file(self):
        for line in fileinput.input([self.filename]):
            decimal, position_one, position_two = line.split(",")
            self.append_dec(decimal, position_one, position_two)
    def append_dec(self, dec, pos_one, pos_two):
        self.numbers.append(Dec_To_Binary(dec, pos_one, pos_two))
    def print_equality(self):
        for n in self.numbers:
            print (n.equality)

def main():
    Bit_Positions(argv[1])

if __name__ == '__main__':
    main()
