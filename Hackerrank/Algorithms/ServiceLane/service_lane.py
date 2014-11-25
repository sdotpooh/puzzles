'''
Author: Sean R. Vinas
Date: 29 Oct 2014
'''
#from sys import argv
import fileinput

def main():
    f = fileinput
    line = f.input()
    line = line.split()
    '''
    while line:
        size = line.split()
        width_array = f.input().split()
        for i in range(int(size[1])):
            limits = f.input().split()
            print(min(width_array[int(limits[0]):int(limits[1])]))
        line = f.input()
    '''




if __name__ == '__main__':
    main()
