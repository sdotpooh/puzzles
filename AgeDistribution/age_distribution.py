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


def main():
    l = ["Still in Mama's arms", 'Preschool Maniac',
         'Elementary school', 'Middle school',
         'High school', 'College',
         'Working for the man', 'The Golden Years',
         "This program is for humans"]
    n = [range(0,3), range(3,5), range(5, 12), range(12, 15), range(15, 19),
         range(19, 23), range(23, 66), range(66, 101)]
    for line in fileinput.input(argv[1]):
        line = line.rstrip('\n')
        if int(line) < 0:
            print(l[8])
        else:
            for x in range(len(n)):
                try:
                    n[x].index(int(line))
                    print(l[x])
                    break
                except ValueError:
                    pass



if __name__ == '__main__':
    main()
