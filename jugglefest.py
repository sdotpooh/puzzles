"""
Author: Sean R. Vinas
email:  vinassr@gmail.com

Solution to yodle Juggle Fest problem
"""
import fileinput
import time

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
    return a*d+b*e+c*f

def galeShapleyAssignmentMatching(cSize, jSize, circuits, jugglers):
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

    return circuits, jugglers

def readInputTextFile(fileName, circuits, jugglers, pListLen):
    for line in fileinput.input([fileName]): 
        if line.strip():
            if line.split()[0] == 'C':
                circuits.append(Circuits(line.split()[1], 
                                         int(line.split()[2].strip('H:')), 
                                         int(line.split()[3].strip('E:')), 
                                         int(line.split()[4].strip('P:'))))
            else:
                jh = int(line.split()[2].strip('H:'))
                je = int(line.split()[3].strip('E:'))
                jp = int(line.split()[4].strip('P:'))
                pList = list(line.split()[5].split(','))
                if pListLen == 0:
                    pListLen = len(pList) # Move out of loop for better speed
                jugglers.append(
                    Jugglers(line.split()[1], jh, je, jp, pList,
                             [dot(jh, je, jp, 
                                  circuits[int(pList[x].strip('C'))].h, 
                                  circuits[int(pList[x].strip('C'))].e, 
                                  circuits[int(pList[x].strip('C'))].p) 
                              for x in xrange(pListLen)]))           
    fileinput.close()
    return circuits, jugglers, pListLen

def sortCircuitsPreferences(cSize, jSize, circuits, jugglers):
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
    return circuits, jugglers

def outputDataToTextFile(cSize, jSize, pListLen, circuits, jugglers):
    f = open("output.txt", "w")
    availablePositions = jSize/cSize
    for xx in xrange(cSize):
        f.write(circuits[xx].name)
        for x in xrange(availablePositions):
            f.write(' ')
            f.write(circuits[xx].partners[x])
            pIndex = int(circuits[xx].partners[x].strip('J'))
            for y in xrange(pListLen):
                f.write(' ')
                f.write(jugglers[pIndex].preferenceList[y])
                f.write(':')
                f.write(str(jugglers[pIndex].dotList[y]))
            if(x != availablePositions - 1):
                f.write(',')
        f.write(' ')
        f.write('\n')
    f.close()
    return

def whoToEmailAtYodle(cSize, jSize, circuitNumber, circuits):
    sol = 0
    cOut = circuitNumber
    for x in xrange(jSize/cSize):
        sol += int(circuits[cOut].partners[x].strip('J'))
    print sol,'@yodle.com'
    return

def main():
    start = time.time()
    circuits = []
    jugglers = []
    fileName = 'jugglefest.txt'
    pListLen = 0

    # Read text file and extract data
    (circuits, jugglers, pListLen) = readInputTextFile(fileName, 
                                                       circuits, 
                                                       jugglers, 
                                                       pListLen)
 
    jSize = len(jugglers)
    cSize = len(circuits)

    # Sort each circuits jugglers by calculating 
    # each dot product, then sorting
    (circuits, jugglers) = sortCircuitsPreferences(cSize, 
                                                   jSize, 
                                                   circuits, 
                                                   jugglers)
    # Gale Shapley Algorithm
    # Matches jugglers to circuits based on prefernces
    # and dot product of skills
    (circuits, jugglers) = galeShapleyAssignmentMatching(cSize, 
                                                         jSize, 
                                                         circuits, 
                                                         jugglers)
     
    # Format output text file to current directory
    # output file = output.txt
    outputDataToTextFile(cSize, jSize, pListLen, circuits, jugglers)
    
    # Email to: 
    # Function sums the jugglers id's to create the who to email
    circuitNumber = 1970
    whoToEmailAtYodle(cSize, jSize, circuitNumber, circuits)
    
    # General time analysis
    stop = time.time()
    print stop - start

if __name__ == '__main__':
    main()


