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

int main()
{
	// Initialization of the output integer (final answer)
	int output = 0;
	// A counter used to detect the 1st entrance into our 
	// testing condition (input >= inM)
	int count = 0; 
	// The multiplier for the input integer/the largest 
	// binary value to achieve N = 1,000,000,000 (2^29)
	int inM  = 536870912; 
	// The multiplier for the output integer
	int outM = 0;   
	int input;
	// Grabs just a single integer from the command line
	cin >> input; 

	// The loop runs until the input is converted to 
	// its binary equivalent (i.e. equals zero)
	// Simultaneously converting it to the inverse 
	// integer reversed binary
	while(input != 0)
	{
		// If input is greater than inM then subtract 
		// that 2^x value to construct its binary equivalent
		if(input >= inM)
		{
			input -= inM;
			if(count == 0)
			{
				outM = 1; 
				count++;
			}			
			output += outM;
		}
		// Reduce the input multiplier by a factor of 2
		inM /= 2;  
		// Increase the output multiplier by a factor of 2
		outM *= 2; 
	}
	cout << output  << endl;
}
