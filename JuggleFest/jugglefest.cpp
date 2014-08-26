/*
Created on 25 July 2014
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
*/
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::stoi;


class Juggler {
	public:
		Juggler();
		Juggler(string, unsigned short int, unsigned short int,
				unsigned short int, 
				vector<string>& preference_list,
				vector<unsigned short int>& dot_list);
		void assign_partner(Juggler &juggler);
		void remove_partner();
		string get_name();
		string get_partner();
		unsigned short int get_endurance();
		unsigned short int get_hand_eye();
		unsigned short int get_pizzazz();
		unsigned short int get_value();
		vector<string> get_preference_list();
		vector<unsigned short int> get_dot_list();
		unsigned short int get_dot(int);
	protected:
		unsigned short int endurance_;
		unsigned short int hand_eye_;
		unsigned short int pizzazz_;
		unsigned short int value_;
		string name_;
		string partner_;
		vector<string> preference_list_;
		vector<unsigned short int> dot_list_;
};


Juggler::Juggler() {

}


Juggler::Juggler(string name, unsigned short int hand_eye,
				 unsigned short int endurance, unsigned short int pizzazz, 
		         vector<string>& preference_list,
				 vector<unsigned short int>& dot_list) {
	name_ = name;
	hand_eye_ = hand_eye;
	endurance_ = endurance;
	pizzazz_ = pizzazz;
	value_ = stoi(name.erase(0,1));
	preference_list_ = preference_list;
	dot_list_ = dot_list;
	partner_.clear();
}


string Juggler::get_name() {
	return name_;
}


unsigned short int Juggler::get_endurance() {
	return endurance_;
}


unsigned short int Juggler::get_hand_eye() {
	return hand_eye_;
}


unsigned short int Juggler::get_pizzazz() {
	return pizzazz_;
}


unsigned short int Juggler::get_value() {
	return value_;
}


vector<string> Juggler::get_preference_list() {
	return preference_list_;
}


vector<unsigned short int> Juggler::get_dot_list() {
	return dot_list_;
}


unsigned short int Juggler::get_dot(int index) {
	return dot_list_.at(index);
}

void Juggler::assign_partner(Juggler &juggler) {
	partner_ = juggler.get_name();
}


string Juggler::get_partner() {
	return partner_;
}


void Juggler::remove_partner() {
	partner_.clear();
}


class Circuit : public Juggler {
	public:
		Circuit();
		Circuit(string, unsigned short int, unsigned short int,
				unsigned short int);
		void assign_dot(unsigned short int);
		void push_partner(string);
		void assign_partner_and_dot(Juggler& juggler);
		void set_positions(unsigned short int);
		void remove_partner_and_dot(Juggler& juggler);
		bool openings();
		unsigned short int get_positions();
		unsigned short int min_partner_dot();
		unsigned short int min_partner_dot_index();
		unsigned short int get_dot(Juggler &juggler);
		unsigned short int get_dot(unsigned short int, unsigned short int, 
								   unsigned short int);
		unsigned short int get_dot_value_at(int);
		vector<string> get_partners_list();
		vector<unsigned short int> get_partners_dot_list();
		string get_partner_at(int);
	protected:
		unsigned short int positions_;
		vector<string> partners_;
		vector<unsigned short int> partners_dot_values_;
};


Circuit::Circuit() {

}


Circuit::Circuit(string name, unsigned short int hand_eye,
				 unsigned short int endurance,
				 unsigned short int pizzazz) {
	name_ = name;
	endurance_ = endurance;
	hand_eye_ = hand_eye;
	pizzazz_ = pizzazz;
	value_ = stoi(name.erase(0, 1));
	positions_ = 0;
}


void Circuit::assign_dot(unsigned short int jugglers_dot) {
	partners_dot_values_.push_back(jugglers_dot);
}


void Circuit::push_partner(string jugglers_name) {
	partners_.push_back(jugglers_name);
}


void Circuit::assign_partner_and_dot(Juggler& juggler) {
	string name = juggler.get_name();
	push_partner(name);
	int dot_value = 0;
	vector<string> p_list = juggler.get_preference_list();
	vector<string>::iterator it;
	
	it = std::find(p_list.begin(), p_list.end(), name);
	if (it == p_list.end())
  		dot_value = get_dot(juggler);
	else
  		dot_value = juggler.get_dot(std::distance(p_list.begin(), it));
	assign_dot(dot_value);
}


unsigned short int Circuit::get_dot_value_at(int index) {
	return partners_dot_values_.at(index);
}


string Circuit::get_partner_at(int index) {
	return partners_.at(index);
}


unsigned short int Circuit::get_dot(Juggler &juggler) {
	return (get_hand_eye()*juggler.get_hand_eye() +
			get_endurance()*juggler.get_endurance() +
			get_pizzazz()*juggler.get_pizzazz());;
}


unsigned short int Circuit::get_dot(unsigned short int hand_eye, 
									unsigned short int endurance, 
									unsigned short int pizzazz) {
	return (get_hand_eye()*hand_eye +
			get_endurance()*endurance +
			get_pizzazz()*pizzazz);;
}


vector<unsigned short int> Circuit::get_partners_dot_list() {
	return partners_dot_values_;
}


vector<string> Circuit::get_partners_list() {
	return partners_;
}


void Circuit::remove_partner_and_dot(Juggler& juggler) {
	vector<string> partners = get_partners_list();
	vector<unsigned short int> partners_dots = get_partners_dot_list();
	vector<string>::iterator it;
	it = std::find(partners.begin(), partners.end(), juggler.get_name());
	int pos = std::distance(partners.begin(), it);
	partners_.erase(partners_.begin() + pos);
	partners_dot_values_.erase(partners_dot_values_.begin() + pos);
}


bool Circuit::openings() {
	if(positions_ - partners_.size() > 0)
		return true;
	else
		return false;
}


unsigned short int Circuit::get_positions() {
 	return positions_;
}


unsigned short int Circuit::min_partner_dot() {
	return get_dot_value_at(min_partner_dot_index());
}


unsigned short int Circuit::min_partner_dot_index() {
	vector<unsigned short int> p_list = get_partners_dot_list();
	vector<unsigned short int>::iterator it;
	it = std::min_element(p_list.begin(), p_list.end());
	return std::distance(p_list.begin(), it);
}


void Circuit::set_positions(unsigned short int positions) {
	positions_ = positions;
}


unsigned short int dot(Juggler &circuit, Juggler &juggler) {
	return (circuit.get_hand_eye()*juggler.get_hand_eye() +
			circuit.get_endurance()*juggler.get_endurance() +
			circuit.get_pizzazz()*juggler.get_pizzazz());
}


void read_input_text_file(string filename, vector<Juggler>& jugglers,
						  vector<Circuit>& circuits) {
	std::ifstream file(filename);
    string str, buf; 
	vector<string> file_line;
    while (std::getline(file, str))
    {
		if(str.compare("") != 0) {
			if(str.front() == 'C') {
				string str1 = str.substr(2, str.length());
				string name, hand_eye, endurance, pizzazz;
				std::istringstream ss(str1);
				ss >> name >> hand_eye >> endurance >> pizzazz;
				unsigned short int h_e, en, piz; 
				h_e = stoi(hand_eye.substr(2, hand_eye.length()));
				en = stoi(endurance.substr(2, endurance.length()));
				piz = stoi(pizzazz.substr(2, pizzazz.length()));
				circuits.push_back(Circuit(name, h_e, en, piz));
			}
			else if(str.front() == 'J') {
				vector<string> pref_list;
				vector<unsigned short int> pref_dot_list;
				string str2 = str.substr(2, str.length());
				string j_name, j_hand_eye, j_endurance, j_pizzazz, p_list;
				std::istringstream ss(str2);
				ss >> j_name >> j_hand_eye >> j_endurance >> j_pizzazz >> p_list;
				unsigned short int h_e, en, piz, j_dot; 
				h_e = stoi(j_hand_eye.substr(2, j_hand_eye.length()));
				en = stoi(j_endurance.substr(2, j_endurance.length()));
				piz = stoi(j_pizzazz.substr(2, j_pizzazz.length()));
				std::stringstream ss_p_list(p_list);
				while(ss_p_list.good()) {
					string substr;
   					getline(ss_p_list, substr, ',');
   					pref_list.push_back(substr);
					string i = substr.erase(0, 1);
					j_dot = circuits[stoi(i)].get_dot(h_e, en, piz);
					pref_dot_list.push_back(j_dot);
				}
				jugglers.push_back(Juggler(j_name, h_e, en, piz, pref_list, 
										   pref_dot_list));
			}	
		}
    }
}


void set_circuit_positions(unsigned short int circuits_size, 
						   unsigned short int jugglers_size, 
						   vector<Circuit>& circuits) {
	unsigned short int number_of_positions = jugglers_size/circuits_size;
	int size = circuits.size();
	for(int i = 0; i < size; ++i)
		circuits[i].set_positions(number_of_positions);
}


void pair_circuit_and_juggler(Circuit& circuit, Juggler& juggler,
							  vector<Juggler>& jugglers, bool& success,
							  unsigned short int& total_open_positions) {
	if(circuit.openings() == true) {
		circuit.assign_partner_and_dot(juggler);
		juggler.assign_partner(circuit);
		--total_open_positions;
		success = true;
		return;
	}
	else {
		if(circuit.get_dot(juggler) > circuit.min_partner_dot()) {
			unsigned short int prev_juggler_index;
			unsigned short int prev_juggler_loc;
			string prev_juggler_loc_s;
			prev_juggler_index = circuit.min_partner_dot_index();
			prev_juggler_loc_s = circuit.get_partners_list()[prev_juggler_index];
			prev_juggler_loc = stoi(prev_juggler_loc_s.substr(1, 
									prev_juggler_loc_s.length()-1));
			circuit.remove_partner_and_dot(jugglers[prev_juggler_loc]);
			jugglers[prev_juggler_loc].remove_partner();
			circuit.assign_partner_and_dot(juggler);
			juggler.assign_partner(circuit);
			success = true;
			return;
		}
	}
	success = false;
}


void assign_within_pref(vector<Circuit>& circuits, vector<Juggler>& jugglers,
		   				Juggler& juggler, bool &success, 
						unsigned short int &total_open_positions) {
	string proposed_circuit;
	unsigned short int preference_size = juggler.get_preference_list().size();
	for (unsigned short i = 0; i < preference_size; i++) {
		proposed_circuit = juggler.get_preference_list()[i];
		pair_circuit_and_juggler(circuits[stoi(proposed_circuit.substr(1,
								 proposed_circuit.length()))],
								 juggler, jugglers, success,
								 total_open_positions);
		if(success == true)
			return;
	}
}


void assign_outside_pref(vector<Circuit>& circuits, vector<Juggler>& jugglers,
		   				Juggler& juggler, bool &success, 
						unsigned short int &total_open_positions) {
	string proposed_circuit;
	unsigned short int circuit_size = circuits.size();
	for (unsigned short i = 0; i < circuit_size; i++) {
		pair_circuit_and_juggler(circuits[i], juggler, jugglers, success,
								 total_open_positions);
		if(success == true)
			return;
	}
}


void gale_shapley_matching(vector<Circuit>& circuits, 
						   vector<Juggler>& jugglers) {
	unsigned short int total_open_positions = jugglers.size();
	unsigned short int jugglers_size = jugglers.size();
	bool success;
	string juggler_partner;
	while (total_open_positions > 0) {
		for (unsigned short i = 0; i < jugglers_size; i++) { 
			success = false;
			juggler_partner = jugglers[i].get_partner();
			if(juggler_partner.empty() == true) {
				assign_within_pref(circuits, jugglers, jugglers[i], success,
								   total_open_positions);
				if(success == true)
					continue;
				else {
					assign_outside_pref(circuits, jugglers, jugglers[i], success,
								   		total_open_positions);
					if(success == true)
						continue;
				}	
			}
		}
	}
}


void output_data_to_text_file() {

}


unsigned short int who_to_email_at_yodle(Circuit& circuit) {
	unsigned short int cum_sum = 0;
	vector<string> partners = circuit.get_partners_list();
	unsigned short int partners_size = partners.size();
	for (unsigned short i = 0; i < partners_size; i++) {
		cum_sum = cum_sum + stoi(partners[i].substr(1, partners[i].length()));
	}
	return cum_sum;
}

void test_circuit_class() {
	// Test the Circuits class
	Circuit circuit("C0", 8, 9, 10);
	assert(circuit.get_name() == "C0");
	assert(circuit.get_value() == 0);
	assert(circuit.get_hand_eye() == 8);
	assert(circuit.get_endurance() == 9);
	assert(circuit.get_pizzazz() == 10);
	circuit.set_positions(2);
	assert(circuit.openings() == true);
	vector<string> circuit_list;
	circuit_list.push_back("C0");
	circuit_list.push_back("C1");
	vector<unsigned short int> circuit_dots;
	circuit_dots.push_back(120);
	circuit_dots.push_back(119);
	Juggler juggler("J0", 10, 9, 8, circuit_list, circuit_dots);
	assert(juggler.get_name() == "J0");
	assert(circuit.get_dot(juggler) == 241);
	circuit.assign_partner_and_dot(juggler);
	assert(circuit.get_dot_value_at(0) == 241);
	assert(circuit.get_partner_at(0) == "J0");
	Juggler juggler1("J1", 1, 1, 1, circuit_list, circuit_dots);
	circuit.assign_partner_and_dot(juggler1);
	assert(circuit.min_partner_dot() == 27);
	assert(circuit.min_partner_dot_index() == 1);
	cout<< "Circuit class tests passed!\n";
}

void test_juggler_class() {
	vector<string> circuit_list;
	circuit_list.push_back("C0");
	circuit_list.push_back("C1");
	vector<unsigned short int> circuit_dots;
	circuit_dots.push_back(120);
	circuit_dots.push_back(119);
	Juggler juggler("J0", 10, 9, 8, circuit_list, circuit_dots);
	assert(juggler.get_name() == "J0");
	assert(juggler.get_value() == 0);
	assert(juggler.get_hand_eye() == 10);
	assert(juggler.get_endurance() == 9);
	assert(juggler.get_pizzazz() == 8);
	Circuit circuit("C0", 8, 9, 10);
	juggler.assign_partner(circuit);
	assert(juggler.get_partner() == "C0");
	juggler.remove_partner();
	assert(juggler.get_partner() == "");
	cout<< "Juggler class tests passed!\n";
}

void test_dot_product() {
	vector<string> circuit_list;
	circuit_list.push_back("C0");
	circuit_list.push_back("C1");
	vector<unsigned short int> circuit_dots;
	circuit_dots.push_back(120);
	circuit_dots.push_back(119);
	Juggler juggler("J0", 10, 9, 8, circuit_list, circuit_dots);
	Circuit circuit("C0", 8, 9, 10);
	assert(dot(circuit, juggler) == 241);
	Circuit circuit_one("C1", 0, 0, 0);
	Juggler juggler_one("J1", 10, 10, 10, circuit_list, circuit_dots);
	assert(dot(circuit_one, juggler_one) == 0);
	Circuit circuit_two("C2", 10, 10, 10);
	Juggler juggler_two("J2", 0, 0, 0, circuit_list, circuit_dots);
	assert(dot(circuit_two, juggler_two) == 0);
	cout<< "dot() tests passed!\n";
}


void test_all() {
	test_circuit_class();
	test_juggler_class();
	test_dot_product();
	vector<Juggler> jugglers;
	vector<Circuit> circuits;
	read_input_text_file("jugglefest.txt", jugglers, circuits);
	set_circuit_positions(circuits.size(), jugglers.size(), circuits);
	gale_shapley_matching(circuits, jugglers);
	cout << who_to_email_at_yodle(circuits[1970]) << "@yodle.com" << endl;
	cout<<"All tests pass!\n";
}


int main(int argc, char *argv[]) {
	if(argc < 2)
		test_all();
	else {
		vector<Juggler> jugglers;
		vector<Circuit> circuits;
		read_input_text_file(argv[1], jugglers, circuits);
		set_circuit_positions(circuits.size(), jugglers.size(), circuits);
		gale_shapley_matching(circuits, jugglers);
		cout << who_to_email_at_yodle(circuits[1970]) <<  endl;
	}
	return 0;
}


