'''
Created on 3 August 2014
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
from copy import copy
from sys import argv
from itertools import combinations


class Issue(object):
    ''' Details of the Issue class:
    Each issue class contains core information about 
    an presidential election. Adding an Issue to a presidential 
    campaign will append State(s) linked to that Issue. When a State
    linked to an Issue wins at least 51%, that State's votes are 
    added to the Issue's votes.'''
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.value = None
        self.votes = None
        states = []
    def set_value(self, value):
        self.value = value if self.value is None else self.value
    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def get_value(self):
        return self.value
    def get_votes(self):
        return self.votes
    def add_votes(self, votes):
        ''' .'''
        self.votes += votes
    def append_state(self, state, value):
        ''' Appends a state to the Issue.
        state: Object
        value: int'''
        state.increment_per(value)
        self.states.append(state)
    def states_votes(self):
        '''for each state fetch votes if any
        Check if state achieved majority 1st
        if it has, check if the state is assigned to an issue
        if it isn't assign it to this issue. Retrieve votes
        '''
        for state in self.states:
            if state.achieved_majority():
                if state.achieved_majority_by() == None:
                    state.set_achieved_majority_by(self)
                    self.add_votes(votes)
        return self.votes


class State(object):
    ''' State class, a State is linked to Issue's. Each State
    contains the votes that contribute to an Election in the 
    electoral college.'''
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes
        self.total_votes
        self.issues = []
        self.achieved_majority = False
        self.achieved_majority_by = None
        self.per = None
        self.percent = None
        self.wins = None
    def set_achieved_majority_by(self, issue):
        self.achieved_majority_by = isuue
    def set_per(self, per):
        self.per = per
    def set_percentage(self, percentage):
        self.percentage = percentage
    def get_name(self):
        return self.name
    def get_votes(self):
        return self.votes
    def get_issues(self):
        return self.issues
    def get_percentage(self):
        #return (self.wins/per)100.0
    def increment_per(self, per):
        self.per += per
    def increment_percentage(self, percentage):
        self.percentage += percentage
    def issues_size(self):
        return len(self.get_issues())
    def append_issue(self, issue, value):
        '''Increment percent by value
        Check if percent is > 50%, if so 
        check if it has been assigned to an issue
        If not, assign it, and send the states votes to it
        After a state has been won, continue to increment percent
        but don't assign to another issue.'''
    def achieved_majority(self):
        '''Only one issue can get the votes
        append the votes to that issue.'''
        return


class Election(object):
    '''Election class, a single Election of collecting votes 
    on (a) issue(s) with State(s).'''
    def __init__(self, issues):
        self.issues = copy(issues)
        self.cost = None
        self.won = False
        self.votes = None
    def sum_states_votes(self):
        '''Go through each state and retrieve votes if
        they are greater than 50%. If the total sum is
        >= 270, set won to true. 
        '''


class Campaign(object):
    '''Campaign class, contains all the voting State's and all the
    Issue's. All possible combinations of Elections will be tried, 
    starting from a single Issue Election, to all Issue's Election, 
    till an Election wins with the fewest and cheapest Issues. 
    Declare the best election strategy (print issues).'''
    def __init__(self, filename):
        self.name 
        self.issues = []
        self.states = []
        self.cost = 0 
        self.won = False
        self.votes = 0
        self.filename = filename
    def read_input_file(self, filename):
        f = open(filename)
        # first line contains number of issues
        line = f.readline()
        f.close()
        return
    def instantiate_issues():
        return

    def instantiate_states():
        return

    def combinations_of_issues(self, issues, choose_r):
        ''' .'''
        #itertools combinations(issues, choose_r)
        return
    def campaign_strategy():
        ''' The core algorithm:
        Incrementally tries Elections based on increasing
        Issue's till an electoral college votes exceed 270, which
        concludes an Election won.'''
        return
    def sum_cost(self):
        ''' .'''
    def print_cost():
        print self.cost
    def print_issues():
        print self.issues
    def print_states():
        print self.states


def test_issue_class():
    ''' Test Issue class functionality.'''
    camp_fin = Issue('Campaign Finance', 726053)
    assert camp_fin.get_name() == 'Campaign Finance', (
    'expected name == Campaign Finance')
    assert camp_fin.get_cost() == 726053, 'expected cost == 726053'
    camp_fin.set_value(3)
    assert camp_fin.get_value() == 3, 'expected value == 3'
    camp_fin.set_value(5)
    assert camp_fin.get_value() == 3, 'expected value == 3'


def test_state_class():
    ''' Test State class functionality.'''
    camp_fin = Issue('Campaign Finance', 726053)
    crime = Issue('Crime', 619414)
    church_state = Issue('Church State', 471764)
    new_york = State('New York', 29)
    assert new_york.get_name() == 'New York', (
        'expected name == New York')
    assert new_york.get_votes() == 29, 'expected votes == 29'
    new_york.append_issue(camp_fin, 4)
    assert new_york.get_issues()[0].get_name() == 'Campaign Finance', (
        'expected state issue name == Campaign Finance')
    assert new_york.get_issues()[0].get_value() == 4, (
        'expected state issue value == 4')
    new_york.append_issue(crime, 7)
    assert new_york.get_issues()[1].get_name() == 'Crime', (
        'expected state issue name == Crime')
    assert new_york.get_issues()[1].get_value() == 7, (
        'expected state issue value == 7')
    new_york.append_issue(church_state, 0)
    assert new_york.get_issues()[2].get_name() == 'Church State', (
        'expected state issue name == Church State')
    assert new_york.get_issues()[2].get_value() == 0, (
        'expected state issue value == 0')
    assert new_york.issues_size() == 3, 'Expected size == 3'
    assert camp_fin.get_value() == None, 'expected value == None'
    assert crime.get_value() == None, 'expected value == None'
    assert church_state.get_value() == None, 'expected value == None'


def test_election():
    ''' Test all Election class functionality.'''


def test_campaign():
    ''' Test all Campaign class functionality.'''


def test_all():
    ''' Test's all classes functionalities.'''
    test_issue_class()
    test_state_class()
    test_election()
    test_campaign()
    print 'All tests pass!'


def main():
    """Main program. Finds the optimal campaign strategy.
    The strategy with the least Issue's and the cheapest."""
    filename = argv[1]
    campaign_strategy = Campaign(filename)
    campaign_strategy.print_issues()


if __name__ == '__main__':
    if len(argv) > 1:
        main()
    else:
        test_all()
