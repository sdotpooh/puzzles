#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using std::cin;
using std::cout;
using std::endl;
using std::ifstream;
using std::string;
using std::stoi;


void dec2bin(unsigned long x) {
	if (x == 0)
		cout << 0 << endl;
	else {
		int c;
		int b = 0;
		for(int i=31; i >=0 ; i--) {
			c =  (x >> i) & 0x1;
			if (c == 1) {
				b = 1;
				cout << '1';
			}
			else if (b == 1)
				cout << '0';
		}
		cout << endl;
	}
}


int main(int argc, char *argv[]) {
	string filename = argv[1];
	std::ifstream file(filename);
	string line;
  	while (std::getline(file, line)) {
		if(line.compare("") != 0)
			dec2bin(stoi(line));
    }
	file.close();
	return 0;
}
