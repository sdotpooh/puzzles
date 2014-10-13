import re
from sys import argv


def main():
    filename = argv[1]
    f = open(filename)
    for line in f:
        if line == '\n':
            pass
        else:
            line = line.strip('\n').split('@')
            if len(line) == 2:
                local = line[0]
                domain = line[1]
                match_domain = re.match(r'([\w]+\.?\b)+', domain)
                if ((match_domain.span()[1] - match_domain.span()[0])
                    == len(domain)):
                    ''' local part:
                        1) (.) cannot be first or last or consecutive
                        2) () cannot be '''
                    match_local = re.match(r'([\w\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\}\~]+\.?\+?\b)+', local)
                    if match_local:
                        if ((match_local.span()[1] - match_local.span()[0])
                            == len(local)):
                            print('true', ': ', line)
                        else:
                            print('false')
                    else:
                        print('false')
                else:
                    print('false')

            elif len(line) > 0:
                print('false')
            else:
                pass


if __name__ == '__main__':
    main()
