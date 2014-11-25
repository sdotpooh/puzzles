'''
Created on 25 June 2014
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


class Circuits(object):
    """Purpose of this class is to store and organize each circuits details.
    A circuit is a team of jugglers.
    Attributes:
        name: a string identifier of the circuit.
        hand_eye: integer of this circuits hand_eye rating.
        endurance: integer of this circuits endurance rating.
        pizzazz: integer of this circuits pizzazz rating.
        partners: list of strings of jugglers names assigned to circuit.
        partners_dot_values: list of integers of partners dot values.
        positions: integer of how many partners the circuit may have.
        value: integer of the circuit name stripped of its 'C'
        min_dot: integer of the min partner dot value
        min_dot_index: integer of the min partner dot index in the list
    """
    def __init__(self, name, hand_eye, endurance, pizzazz):
        """Initializes the circuit with basic information."""
        self.name = name
        self.hand_eye = hand_eye
        self.endurance = endurance
        self.pizzazz = pizzazz
        self.partners = []
        self.partners_dot_values = []
        self.positions = None #I can store this externally just once!
        self.value = int(self.name.strip('C'))
    def assign_partner_and_dot(self, juggler):
        """Assign the juggler
        juggler = Object"""
        self._assign_partner(juggler.name)
        dot_value = None
        #Try circuit in preference list:
        try:
            dot_index = juggler.preference_list.index(self.name)
            dot_value = juggler.dot_list[dot_index]
            self._assign_dot(dot_value)
        except ValueError: #If not in list, calculate the dot
            dot_value = self.dot(juggler)
            self._assign_dot(dot_value)
    def dot(self, juggler):
        """ juggler = Object of Juggle Class."""
        return ((self.hand_eye*juggler.hand_eye) +
                (self.endurance*juggler.endurance) +
                (self.pizzazz*juggler.pizzazz))

    def _assign_dot(self, dot):
        """ Append the jugglers dot value.
        dot = Int"""
        self.partners_dot_values.append(dot)
    def _assign_partner(self, juggler_name):
        """ Assign the juggler as a partner.
        juggler.name = String"""
        self.partners.append(juggler_name)
    def openings(self):
        """Returns a Boolean if open positions available"""
        if self.positions-len(self.partners) > 0:
            return True
        else:
            return False
    def remove_partner_and_dot(self, juggler):
        """Removes a specific juggler name and dot value from
        the list partners and the list partners_dot_values.
        juggler = Object"""
        try:
            pos = self.partners.index(juggler.name)
        except IndexError:
            print ('Remove circuit partner IndexError')
        self.partners.pop(pos)
        self.partners_dot_values.pop(pos)
    def min_partner_dot(self):
        """ Returns the value of the min dot juggler."""
        return min(self.partners_dot_values)
    def min_partner_dot_index(self):
        """Returns the index of the min dot partner."""
        return self.partners_dot_values.index(min(self.partners_dot_values))


class Jugglers(object):
    """Purpose of this class is to store and organize each jugglers details.

    A juggler is an individual who is assigned to a circuit.
    Attributes:
        name: a string identifier of the circuit.
        hand_eye: integer of this circuits hand_eye rating.
        endurance: integer of this circuits endurance rating.
        pizzazz: integer of this circuits pizzazz rating.
        preference_list: list of strings of circuits in preferred order.
        dot_list: list of integers of dot values for preference_list
        partner: list of strings of jugglers names assigned to circuit.
        next_on_list: integer of the next preferred circuit
    """
    def __init__(self, name, hand_eye, endurance, pizzazz,
                 preference_list, dot_list):
        self.name = name
        self.hand_eye = hand_eye
        self.endurance = endurance
        self.pizzazz = pizzazz
        self.preference_list = preference_list
        self.dot_list = dot_list
        self.partner = None
        self.value = int(self.name.strip('J'))
    def assign_partner(self, circuit):
        """ Assign the circuit & juggler as partners.
        circuit: Object"""
        # Assign the circuit as jugglers partner
        self.partner = circuit.name
    def remove_partner(self):
        """ Remove partner."""
        self.partner = None


def dot(vector_a_one, vector_a_two, vector_a_three, vector_b_one,
        vector_b_two, vector_b_three):
    """Returns an integer dot product."""
    return (vector_a_one*vector_b_one + vector_a_two*vector_b_two +
            vector_a_three*vector_b_three)


def read_input_text_file(filename, circuits, jugglers, pref_list_len):
    """Reads a text file and populates circuits and jugglers with data.
    One line per circuit or juggler. All circuits will come before any
    jugglers. Circuit lines start with a C and juggler lines start with a J.
    Names of circuits and jugglers will never have spaces. A skill and the
    rating for that skill are separated by a colon. Circuit lines have the
    circuit names followed by skills. Juggler lines have the juggler names
    followed by skills, followed by circuits in order of preference, separated
    by commas. Example:
    C C0 H:7 E:7 P:10
    C C1 H:2 E:1 P:1
    C C2 H:7 E:6 P:4

    J J0 H:3 E:9 P:2 C2,C0,C1
    J J1 H:4 E:3 P:7 C0,C2,C1
    J J2 H:4 E:0 P:10 C0,C2,C1
    ...
    """
    for line in fileinput.input([filename]):
        if line.strip():
            if line.split()[0] == 'C':
                circuits.append(Circuits(line.split()[1],
                                         int(line.split()[2].strip('H:')),
                                         int(line.split()[3].strip('E:')),
                                         int(line.split()[4].strip('P:'))))
            else:
                jugglers_h = int(line.split()[2].strip('H:'))
                jugglers_e = int(line.split()[3].strip('E:'))
                jugglers_p = int(line.split()[4].strip('P:'))
                pref_list = list(line.split()[5].split(','))
                if pref_list_len == 0:
                    pref_list_len = len(pref_list)
                temp = [dot(jugglers_h, jugglers_e, jugglers_p,
                            circuits[int(pref_list[x].strip('C'))].hand_eye,
                            circuits[int(pref_list[x].strip('C'))].endurance,
                            circuits[int(pref_list[x].strip('C'))].pizzazz)
                        for x in range(pref_list_len)]
                jugglers.append(Jugglers(line.split()[1], jugglers_h,
                                         jugglers_e, jugglers_p, pref_list,
                                         temp))
                del temp
    fileinput.close()
    return circuits, jugglers, pref_list_len


def set_circuit_positions(circuits_size, jugglers_size, circuits):
    """Assigns each circuit an amount of positions it needs to fill."""
    number_of_positions = jugglers_size/circuits_size
    for circuit in circuits:
        circuit.positions = number_of_positions
    return circuits


def gale_shapley_matching(jugglers_size, circuits, jugglers):
    """Gale-Shapley algorithm.
    when assigning jugglers to circuits we also want to consider how well
    their skills match up to the circuit. In fact we want to match jugglers
    to circuits such that no juggler could switch to a circuit that they
    prefer more than the one they are assigned to and be a better fit for that
    circuit than one of the other jugglers assigned to it."""
    total_open_positions = jugglers_size
    while total_open_positions > 0:
        for juggler in jugglers:
            success = False
            if juggler.partner == None:
                [circuits, jugglers, success, total_open_positions] = (
                    assign_within_pref(circuits, juggler, jugglers,
                                       success, total_open_positions))
                if success:
                    continue
                else:
                    [circuits, jugglers, success, total_open_positions] = (
                        assign_outside_pref(circuits, juggler, jugglers,
                                            success, total_open_positions))
                    if success:
                        continue

    return circuits, jugglers


def assign_within_pref(circuits, juggler, jugglers, success,
                       total_open_positions):
    """
    circuits = Objects
    juggler = Object
    total_open_positions = Int"""
    for circuit in juggler.preference_list:
        proposed_circuit = circuits[int(circuit.strip('C'))]
        [success, total_open_positions] = pair_circuit_and_juggler(
            proposed_circuit, juggler, jugglers, success,
            total_open_positions)
        if success:
            return circuits, jugglers, success, total_open_positions
    return circuits, jugglers, success, total_open_positions


def assign_outside_pref(circuits, juggler, jugglers, success,
                        total_open_positions):
    """
    juggler = Object
    circuits = Objects
    """
    for circuit in circuits:
        if circuit not in juggler.preference_list:
            [success, total_open_positions] = (
                pair_circuit_and_juggler(circuit, juggler, jugglers, success,
                                         total_open_positions))
            if success:
                return circuits, jugglers, success, total_open_positions
    return circuits, jugglers, success, total_open_positions


def pair_circuit_and_juggler(circuit, juggler, jugglers, success,
                             total_open_positions):
    """
    circuit = Object
    juggler = Object
    success = Boolean
    ."""
    if circuit.openings():
        circuit.assign_partner_and_dot(juggler) #method will find dot
        juggler.assign_partner(circuit)
        total_open_positions -= 1
        success = True
        return success, total_open_positions
    else:
        if circuit.dot(juggler) > circuit.min_partner_dot():
            prev_juggler_indx = circuit. min_partner_dot_index()
            prev_juggler_loc = circuit.partners[prev_juggler_indx].strip('J')
            prev_juggler = jugglers[int(prev_juggler_loc)]
            circuit.remove_partner_and_dot(prev_juggler)
            prev_juggler.remove_partner()
            #Then pair them
            circuit.assign_partner_and_dot(juggler) #method will find dot
            juggler.assign_partner(circuit)
            success = True
            return success, total_open_positions
    success = False
    return success, total_open_positions


def output_data_to_text_file(circuits_size, jugglers_size, pref_list_len,
                             circuits, jugglers):
    """One line per circuit assignment. Each line should contain the circuit
    name followed by the juggler name, followed by that juggler's circuits in
    order of preference and the match score for that circuit. The line should
    include all jugglers matched to the circuit. The example below is a valid
    assignment for the input file above.

    C2 J6 C2:128 C1:31 C0:188, J3 C2:120 C0:171 C1:31, J10 C0:120 C2:86 C1:21,
    J0 C2:83 C0:104 C1:17
    C1 J9 C1:23 C2:86 C0:94, J8 C1:21 C0:100 C2:80, J7 C2:75 C1:20 C0:106,
    J1 C0:119 C2:74 C1:18
    C0 J5 C0:161 C2:112 C1:26, J11 C0:154 C1:27 C2:108, J2 C0:128 C2:68 C1:18,
    J4 C0:122 C2:106 C1:23."""
    outfile = open("./output.txt", "w")
    available_positions = jugglers_size/circuits_size
    for circuit_num in range(circuits_size):
        outfile.write(circuits[circuit_num].name)
        for position_num in range(available_positions):
            outfile.write(' ')
            outfile.write(circuits[circuit_num].partners[position_num])
            pref_index = int(
                circuits[circuit_num].partners[position_num].strip('J'))
            for pref_num in range(pref_list_len):
                outfile.write(' ')
                outfile.write(jugglers[pref_index].preference_list[pref_num])
                outfile.write(':')
                outfile.write(str(jugglers[pref_index].dot_list[pref_num]))
            if position_num != available_positions-1:
                outfile.write(',')
        outfile.write(' ')
        outfile.write('\n')
    outfile.close()
    return


def who_to_email_at_yodle(circuit):
    """Send  to the following e-mail address:
    the sum of the names of the jugglers (taking off the leading letter J)
    that are assigned to circuit @yodle.com.
    """
    cum_sum = 0
    for juggler_name in circuit.partners:
        cum_sum += int(juggler_name.strip('J'))
    return str(cum_sum) + '@yodle.com'


def test_all():
    """Test all functionality."""
    #Test the Jugglers class.
    jugglers = []
    #Instantiate a juggler
    jugglers.append(Jugglers('J0', 3, 9, 2, ['C2', 'C1', 'C0'],
                             [100, 45, 22]))

    assert jugglers[0].name == 'J0', "expected == 'J0'"
    assert jugglers[0].value == 0, "expected == 0"
    jugglers[0].partner = 'C0'
    assert jugglers[0].hand_eye == 3, 'expected h == 3'
    assert jugglers[0].endurance == 9, 'expected e == 9'
    assert jugglers[0].pizzazz == 2, 'expected p == 2'
    assert jugglers[0].preference_list == ['C2', 'C1', 'C0'], (
        "expected list == ['C2', 'C1', 'C0']")
    assert jugglers[0].dot_list == [100, 45, 22], (
        'expected list == [100, 45, 22]')

    #Test the Circuits class.
    circuits = []
    #Instantiate a circuit
    circuits.append(Circuits('C0', 7, 8, 9))
    assert circuits[0].name == 'C0', "expected == 'C0'"
    assert circuits[0].value == 0, "expected == 0"
    assert circuits[0].hand_eye == 7, 'expected h == 7'
    assert circuits[0].endurance == 8, 'expected e == 8'
    assert circuits[0].pizzazz == 9, 'expected p == 9'
    circuits[0].assign_partner_and_dot(jugglers[0])
    assert circuits[0].partners[:] == ['J0'], "expected list == ['J0']"
    assert circuits[0].partners_dot_values[:] == [22], (
        'expected list == [22]')
    circuits[0].positions = 4
    assert circuits[0].positions == 4, 'expected 4'
    assert circuits[0].openings() == True, 'expected True'
    circuits.append(Circuits('C4', 10, 9, 8))
    jugglers.append(Jugglers('J4', 8, 9, 10, ['C2', 'C1', 'C3'],
                             [100, 45, 22]))

    # Test assign_partner_and_dot method
    circuits[1].assign_partner_and_dot(jugglers[1])
    circuits[1].positions = 2
    assert circuits[1].partners[:] == ['J4'], (
        "%s partners list expected == ['J4']" %circuits[1].name)
    assert circuits[1].partners_dot_values[:] == [241], (
        'expected list == [241]')
    circuits[1].assign_partner_and_dot(jugglers[0])
    assert circuits[1].partners[:] == ['J4', 'J0'], (
        "expected list == ['J4','J0']")
    assert circuits[1].partners_dot_values[:] == [241, 127], (
        'expected list == [241, 127]')
    assert circuits[1].openings() == False, (
        'expected False, %s should have no openings' %circuits[1].name)

    # test circuits dot method
    assert circuits[0].dot(jugglers[0]) == 111, (
        'expected 111, %s dot with %s'
        %(circuits[0].name, jugglers[0].name))
    assert circuits[0].dot(jugglers[1]) == 218, (
        'expected 218, %s dot with %s'
        %(circuits[0].name, jugglers[1].name))
    assert circuits[1].dot(jugglers[0]) == 127, (
        'expected 127, %s dot with %s'
        %(circuits[1].name, jugglers[0].name))
    assert circuits[1].dot(jugglers[1]) == 241, (
        'expected 241, %s dot with %s'
        %(circuits[0].name, jugglers[0].name))

    #Test circuits remove_partner_and_dot method
    circuits[1].remove_partner_and_dot(jugglers[0])
    assert circuits[1].partners[:] == ['J4'], "expected list == ['J4']"
    assert circuits[1].partners_dot_values[:] == [241], (
        'expected list == [241]')

    #Test juggler assign_partner method
    jugglers[0].assign_partner(circuits[0])
    assert jugglers[0].partner == 'C0', "Expected 'C0'"

    #Test juggler remove_partner method
    jugglers[0].remove_partner()
    assert jugglers[0].partner == None, 'Expected None'

    #Test the circuits min_partner_dot method
    assert circuits[0].min_partner_dot() == 22, (
        'expected 22, as the min dot value in %s partners_dot_values'
        %circuits[0].name)
    assert circuits[1].min_partner_dot() == 241, (
        'expected 241, as the min dot value in %s partners_dot_values'
        %circuits[1].name)

    #Test circuits min_partner_dot_index method
    assert circuits[0].min_partner_dot_index() == 0, (
        'expected 0, as the min dot index in %s partners_dot_values'
        %circuits[0].name)
    assert circuits[1].min_partner_dot_index() == 0, (
        'expected 0, as the min dot index in %s partners_dot_values'
        %circuits[1].name)

    #Test the dot product function.
    assert dot(1, 2, 3, 4, 5, 6) == 32, 'expected == 32'
    assert dot(0, 0, 0, 1, 2, 3) == 0, 'expected == 0'
    assert dot(1, 2, 3, 0, 0, 0) == 0, 'expected == 0'

    #Test pair_circuit_and_juggler function, with one opening left
    circuits[0].positions = 2
    success = False
    total_open_positions = 1
    [success, total_open_positions] = (
        pair_circuit_and_juggler(circuits[0], jugglers[1], jugglers, success,
                                 total_open_positions))
    assert circuits[0].partners[:] == ['J0', 'J4'], (
        "expected list == ['J0','J4']")
    assert circuits[0].partners_dot_values[:] == [22, 218], (
        'expected list == [22, 218]')
    assert total_open_positions == 0, 'expected = 0'

    #Test pair_circuit_and_juggler function, with no openings
    jugglers.append(Jugglers('J1', 20, 19, 20, ['C0', 'C1', 'C2'],
                             [300, 45, 22]))

    [success, total_open_positions] = (
        pair_circuit_and_juggler(circuits[0], jugglers[2], jugglers, success,
                                 total_open_positions))

    assert circuits[0].partners[:] == ['J4', 'J1'], (
        "expected list == ['J4','J1']")
    assert circuits[0].partners_dot_values[:] == [218, 300], (
        'expected list == [218, 300]')

    #Test who_to_email_at_yodle function
    assert who_to_email_at_yodle(circuits[0]) == '5@yodle.com', (
        'expected  == 5@yodle.com')

    print ('All tests passed')

#@profile
def main():
    """main program."""
    circuits = []
    jugglers = []
    filename = argv[1]
    pref_list_len = 0

    (circuits, jugglers, pref_list_len) = read_input_text_file(filename,
                                                               circuits,
                                                               jugglers,
                                                               pref_list_len)

    jugglers_size = len(jugglers)
    circuits_size = len(circuits)
    circuits = set_circuit_positions(circuits_size, jugglers_size, circuits)

    (circuits, jugglers) = gale_shapley_matching(jugglers_size, circuits,
                                                 jugglers)

    output_data_to_text_file(circuits_size, jugglers_size, pref_list_len,
                             circuits, jugglers)

    circuit_number = 1970
    print (who_to_email_at_yodle(circuits[circuit_number]))


if __name__ == '__main__':
    if len(argv) > 1:
        main()
    else:
        test_all()
