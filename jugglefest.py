"""
Author: Sean R. Vinas
email:  vinassr@gmail.com

Solution to yodle Juggle Fest problem
"""
import fileinput

class Circuits:
    def __init__(self, name, h, e, p):
        self.name = name
        self.h = h
        self.e = e
        self.p = p
        self.partners  = []   #List of partners
        self.pDots     = []   #List of respective partners dot values
        self.positions = None #How many open positions left
        self.preferenceList = []
    def openings(self):
        return self.positions-len(self.partners)
    def removePartner(self, pos):
        #Remove specific partner and dot value
        self.partners.pop(pos)
        self.pDots.pop(pos)
 
class Jugglers:
    def __init__(self, name, h, e, p, preferenceList, dotList):
        self.name = name
        self.h = h
        self.e = e
        self.p = p
        self.partner = None #Juggler gets only 1 partner
        self.preferenceList = preferenceList
        self.dotList = dotList


def dot(a, b, c, d, e, f):
    return (int(a)*int(d))+(int(b)*int(e))+(int(c)*int(f))

def main():
    circuits = []
    jugglers = []
    filename = 'jugglefest.txt'

    # Read text file and add data
    for line in fileinput.input([filename]): 
        if line.strip():
            if line.split()[0] == 'C':
                circuits.append(Circuits(line.split()[1], 
                                         line.split()[2].strip('H:'), 
                                         line.split()[3].strip('E:'), 
                                         line.split()[4].strip('P:')))
            else:
                jh = line.split()[2].strip('H:')
                je = line.split()[3].strip('E:')
                jp = line.split()[4].strip('P:')
                pList = list(line.split()[5].split(','))
                jugglers.append(
                    Jugglers(line.split()[1], jh, je, jp, pList,
                             [dot(jh, je, jp, 
                                  circuits[int(pList[x].strip('C'))].h, 
                                  circuits[int(pList[x].strip('C'))].e, 
                                  circuits[int(pList[x].strip('C'))].p) 
                              for x in xrange(len(pList))]))           
    fileinput.close()

    # Build a list of tuples of Sorted jugglers 
    jSize = len(jugglers)
    cSize = len(circuits)
    availablePositions = jSize/cSize
    for i in xrange(cSize):
        # Assign each circuit its dot sorted preferenceList
        # as a List of Tuples; highest ranking at the end
        circuits[i].preferenceList = (
            sorted(zip([dot(circuits[i].h,
                            circuits[i].e,
                            circuits[i].p,
                            jugglers[j].h, 
                            jugglers[j].e, 
                            jugglers[j].p) 
                         for j in xrange(jSize)], 
                        [jugglers[k].name for k in xrange(jSize)])))

        # Assign each circuit with a quantity of openings available (J/C)
        circuits[i].positions = availablePositions

    # Gale Shapley - Matching Algorithm
    totalOpenPositions = jSize
    i = -1
    while totalOpenPositions > 0:
        i += 1
        if i == cSize:
            i = 0 # Loop around
        c = circuits[i]
        while c.openings() > 0:
            proposedJuggler = c.preferenceList.pop()
            j = proposedJuggler[1]
            d = proposedJuggler[0]
            jIndex  = jugglers[int(j.strip('J:'))]
            partner = jIndex.partner
            if partner is None:
                c.partners.append(j)
                c.pDots.append(d)
                jIndex.partner = c.name
                totalOpenPositions -= 1
            else: 
                cIndex = circuits[int(jIndex.partner.strip('C'))]
                try:
                    proposed = jIndex.preferenceList.index(c.name)
                except:
                    proposed = None
                try:
                    current  = jIndex.preferenceList.index(partner)
                except:
                    current = None
                if current is not None and proposed is not None:
                    if current > proposed:
                        c.partners.append(j)
                        c.pDots.append(d)
                        cIndex.partners.remove(j)
                        jIndex.partner = c.name
                elif proposed is not None and current is None: 
                    # Choose proposed (on pref list)
                    c.partners.append(j)
                    c.pDots.append(d)
                    cIndex.partners.remove(j)
                    jIndex.partner = c.name
                else:
                    partnersDot = dot(cIndex.h, cIndex.e, cIndex.p, 
                                      jIndex.h, jIndex.e, jIndex.p)
                    # proposed dot product better, choose proposed
                    if d > partnersDot: 
                        c.partners.append(j)
                        c.pDots.append(d)
                        cIndex.partners.remove(j)
                        jIndex.partner = c.name
                    

    # Format output text file
    f = open("output.txt", "w")
    for xx in xrange(cSize):
        f.write(circuits[xx].name)
        for x in xrange(availablePositions):
            f.write(' ')
            f.write(circuits[xx].partners[x])
            pIndex = int(circuits[xx].partners[x].strip('J'))
            for y in xrange(len(jugglers[pIndex].preferenceList)):
                f.write(' ')
                f.write(jugglers[pIndex].preferenceList[y])
                f.write(':')
                f.write(str(jugglers[pIndex].dotList[y]))
            if(x != availablePositions - 1):
                f.write(',')
        f.write(' ')
        f.write('\n')
    f.close()
    
    # Email to: 
    sol = 0
    cOut = 1970
    for x in xrange(availablePositions):
        sol += int(circuits[cOut].partners[x].strip('J'))
    print circuits[cOut].name, sol
    print sol,'@yodle.com'


if __name__ == '__main__':
    main()

