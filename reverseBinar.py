"""
Author: Sean R.Vinas
email: vinassr@gmail.com
"""
import random
import time

def reverseBinary(x):
    xMaxMultiplier = 536870912 # 2^29
    outMultiplier = 0
    output = 0
    count = 0
    while x != 0:
        if x >= xMaxMultiplier:
            x -= xMaxMultiplier
            if count == 0:
                outMultiplier = 1
                count += 1
            output += outMultiplier
        xMaxMultiplier /= 2
        outMultiplier *= 2
    return output


def main():
    cases = 10000000
    randLowerRange = 1
    randUpperRange = 1000000000
    t = 0
    for i in xrange(cases):
        start = time.time()
        reverseBinary(random.randint(randLowerRange, randUpperRange))
        stop = time.time()
        t += stop - start
    print t/cases
    """
    Average time for 10,000,000 cases = 2.48877e-05 s
    """


if __name__ == '__main__':
    main()
