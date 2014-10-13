from sys import argv


def main():
    filename = argv[1]
    f = open(filename)
    for line in f:
        line = line.split()
        cycle_end = line.index(line[-1])
        i = len(line) - 2
        while i > 0:
            if line.index(line[i]) < i and line[i] != line[cycle_end]:
                i -= 1

            else:
                cycle_begin = line.index(line[i+1])
                new_list = line[cycle_begin:cycle_end+1]
                for i in new_list:
                    print(i, end=' ')
                print()
                break



if __name__ == '__main__':
    main()
