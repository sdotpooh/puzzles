'''
Created on 25 August 2014
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
from copy import deepcopy
from sys import argv
from itertools import combinations


class NameMethods(object):
    ''' Define set, get, and print methods for self.name shared in various
    classes.'''
    def __init__(self, name):
        self.name = name
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def print_name(self):
        print self.name


class VotesMethods(object):
    ''' Define set, get, and print methods for self.votes shared in various
    classes.'''
    def __init__(self, votes):
        self.votes = votes
    def set_votes(self, votes):
        self.votes = votes
    def get_votes(self):
        return self.votes
    def print_votes(self):
        print self.votes


class CostMethods(object):
    ''' Define set, get, and print methods for self.cost shared in various
    classes.'''
    def __init__(self, cost):
        self.cost = cost
    def set_cost(self, cost):
        self.cost = cost
    def get_cost(self):
        return self.cost
    def print_cost(self):
        print self.cost
    def increment_cost(self, cost):
        self.set_cost(cost + self.get_cost())


class ObjectsMethods(object):
    ''' Define set, get, and print methods for self.objects shared in various
    classes.'''
    def __init__(self, objs):
        self.objects = objs
    def append_object(self, value):
        self.objects.append(value)
    def get_objects(self):
        return self.objects
    def print_objects(self):
        for obj in self.objects:
            print obj.name
    def sort_alpha_print(self):
        temp_list = []
        for obj in self.objects:
            temp_list.append(obj.name)
        temp_list.sort()
        for name in temp_list:
            print name


class State(NameMethods, VotesMethods):
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.issues_value_cumsum = 0
        self.issues_value_limit = 0
        self.winning_threshold = 51
        self.winning_percent = 0
        self.votes_distributed = False
    def set_issues_value_cumsum(self, value):
        self.issues_value_cumsum = value
    def set_issues_value_limit(self, value):
        self.issues_value_limit = value
    def set_winning_percent(self, percent):
        self.winning_percent = percent
    def set_votes_distributed(self, status):
        self.votes_distributed = status
    def get_issues_value_cumsum(self):
        return self.issues_value_cumsum
    def get_issues_value_limit(self):
        return self.issues_value_limit
    def get_winning_threshold(self):
        return self.winning_threshold
    def get_winning_percent(self):
        return self.winning_percent
    def get_votes_distributed(self):
        return self.votes_distributed
    def print_issues_value_cumsum(self):
        print self.issues_value_cumsum
    def print_issues_value_limit(self):
        print self.issues_value_limit
    def print_winning_threshold(self):
        print self.winning_threshold
    def print_winning_percent(self):
        print self.winning_percent
    def print_votes_distributed(self):
        print votes_distributed
    def add_issue_value(self, value):
        self.set_issues_value_cumsum(value + self.get_issues_value_cumsum())
        self.update_percent()
    def update_percent(self):
        part = float(self.get_issues_value_cumsum())
        quantity = float(self.get_issues_value_limit())
        percent = 100*part/quantity
        self.set_winning_percent(percent)


class Issue(NameMethods, CostMethods, VotesMethods, ObjectsMethods):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.votes = 0
        self.objects = []
        self.states_weights = {} 
    def get_states_weights(self):
        return self.states_weights
    def get_state_weight(self, state_name):
        return self.states_weights[state_name]
    def append_state_weight(self, state_name, weight):
        self.states_weights[state_name] = weight
    def print_weights(self):
        for w in self.states_weights.values():
            print w
    def print_states_w_weights(self):
        for key, value in self.states_weights.iteritems() :
            print key, value


class Election(VotesMethods, CostMethods, ObjectsMethods):
    def __init__(self, issues):
        self.objects = deepcopy(issues)
        self.votes = 0
        self.cost = 0
        self.solicit_issues()
    def solicit_vote(self, state):
        if state.get_winning_percent() >= state.get_winning_threshold():
                    if state.get_votes_distributed() == False:
                        #state.print_name()
                        state.set_votes_distributed(True)
                        self.votes += state.get_votes()
    def solicit_states(self, issue):
        for state in issue.objects:
            state_weight = issue.get_state_weight(state.get_name())
            state.add_issue_value(state_weight)
            self.solicit_vote(state)           
    def solicit_issues(self):
        for issue in self.objects:
            self.solicit_states(issue)
            self.increment_cost(issue.get_cost())



class Campaign(NameMethods, ObjectsMethods):
    def __init__(self, filename):
        self.name = filename
        self.objects = []
        self.optimal_election = None
        self.electoral_threshold = 270
        self.read_file(filename)
        self.try_all_issue_combinations()
        #Print winning strat
        self.optimal_election.sort_alpha_print()
        #self.optimal_election.print_votes()
        #self.optimal_election.print_cost()
    def read_issue_size(self, file_handle):
        line = file_handle.readline()
        issues_size =  line[line.find(':')+2:line.find('\n')]
        file_handle.readline()
        return issues_size
    def read_issues(self, issues_size, file_handle):
        for l in xrange(int(issues_size)):
            line = file_handle.readline()
            loc = line.find(':')
            obj = line[:loc].rstrip('\n')
            cost = line[loc+2:].rstrip('\n')
            self.append_object(Issue(obj, int(cost)))
        file_handle.readline()
    def read_state(self, file_handle):
        state_name = file_handle.readline().rstrip('\n')
        line = file_handle.readline()
        loc = line.find(':')
        vote_size = int(line[loc+2:].rstrip('\n'))
        state = State(state_name, vote_size)
        return state
    def read_states(self, file_handle, size):
        for s in xrange(size):
            state = self.read_state(file_handle)
            weight_sum = 0
            for issue in self.objects:
                line = file_handle.readline()
                loc = line.find(':')
                weight = int(line[loc+2:line.find('\n')])
                weight_sum += weight
                if weight > 0:
                    issue.append_object(state)
                    issue.append_state_weight(state.get_name(), weight)
            state.set_issues_value_limit(weight_sum)
            file_handle.readline()
    def read_file(self, filename):
        file_handle = open(filename)
        issues_size = self.read_issue_size(file_handle)
        self.read_issues(issues_size, file_handle)
        self.read_states(file_handle, 51)
        file_handle.close()
    def compare_elections(self, election):
        if self.optimal_election == None:
            self.optimal_election = election
        elif len(self.optimal_election.objects) < len(election.objects):
            return
        elif len(self.optimal_election.objects) == len(election.objects):
            if self.optimal_election.get_cost() <= election.get_cost():
                return
        self.optimal_election = election
    def try_all_issue_combinations(self):
        for r in xrange(1,len(self.objects)):
            for c in combinations(self.objects, r):
                #if an optimal exists already, test an election that 
                election = Election(list(c))
                if election.get_votes() >= self.electoral_threshold:
                    self.compare_elections(election)
            if self.optimal_election != None:
                return


def test_NameMethods_class():
    pass


def test_VotesMethods_class():
    pass


def test_CostMethods_class():
    pass


def test_ObjectsMethods_class():
    pass


def test_state():
    new_york = State('New York', 20)
    print 'State class passed all tests!'


def test_issue():
    crime = Issue('Crime') 
    print 'Issue class passed all tests!'


def test_election():
    print 'Election class passed all tests!'


def test_campaigne():
    print 'Campaign class passed all tests!'


def test_all():
    test_state()
    test_issue()
    print 'All tests pass!'


def main():
    """Main program. Finds the optimal campaign strategy.
    The strategy with the least Issue's and the cheapest."""
    filename = argv[1]
    Campaign(filename)
    

if __name__ == '__main__':
    if len(argv) > 1:
        main()
    else:
        test_all()
