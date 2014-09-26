// By: Sean R Vinas
// Spotify reversed binary numbers puzzle
// Date: 2/10/2013
//
// Task: Write a program for reversing numbers (integer) in binary. 
// For example input = 13 (1101) and output = 11 (1011)
// Input: 1 line with 1 Int N, 1 <= N <= 1,000,000,000
// Output: 1 line with 1 Int

#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int reverseBinary(int input)
{
	int output = 0;
	int count  = 0; 
	int outputMultiplier = 0;
	// Upper bound = 1,000,000,000 = 2^29 = 536870912
	int inputMultiplier = 536870912;
	while(input != 0) {
		// If input is greater than inputMultiplier then subtract 
		// that 2^x value to construct its binary equivalent
		if(input >= inputMultiplier) {
			input -= inputMultiplier;
			if(count == 0) {
				outputMultiplier = 1; 
				count++;
			}			
			output += outputMultiplier;
		}
		inputMultiplier  /= 2;  
		outputMultiplier *= 2; 
	}
	return output;
}

int main()
{
	int input;
	// Grabs just a single integer from the command line
	cin >> input; 
	int output = reverseBinary(input); 
	cout << output  << endl;
}
