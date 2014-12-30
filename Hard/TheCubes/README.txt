THE CUBES
https://www.codeeval.com/open_challenges/175/
CHALLENGE DESCRIPTION:

You are given a scheme of the labyrinth in the form of a cube with N levels of N × N elements. The walls are marked with asterisks ‘*’, and the floor — with spaces. The floor of different levels, except the lowest one, can have holes marked with ‘o’. The holes allow you to move to a lower level (if it is on the floor of the current level), to move to a higher level (if it is on the floor of the higher level), or to move over the hole on the current level.

Below is the example of a labyrinth scheme for N=5:

Level 1:

*****
*   *
* ***
*   *
** **



Level 2:

*****
*  o*
*o* *
* * *
*****



Level 3:

*****
*   *
* * *
*o* *
*****



Level 4:

*****
* o *
*** *
*   *
*****



Level 5:

** **
*o  *
***o*
*o  *
*****
Find the number of steps in the shortest way from the entrance on the first floor to the exit on the last floor, including entrance and exit. Moving between levels is one step.

INPUT SAMPLE:

The first argument is a file that contains test cases, one test case per line. Each test case contains N number (the length of the cube edge) and scheme of the labyrinth, separated by semicolon. The scheme of the labyrinth is serialized: all elements are listed sequentially, starting from the top left corner of the first level.

For example (the first test case represent the example provided above in challenge description):

5;******   ** ****   *** ********  o**o* ** * ************   ** * 
**o* ************ o **** **   ******** ***o  ****o**o  ******
5;****** * ** * **   *** ********o*o** *o**   ************   **o* 
** *o************   **** **   ******** *** o ****o**  o******
7;********     ** *** ** * * ** * * **     **** *********** *   ** 
*** **   *o**o***o**oo   ****************  oo ** * * ** * * ** * * 
** *o o****************     ** * ****o* * ** *** **o    **********
******     ** *** **     ****** ** o  o**************** *oo ** *** 
**o  * ** *** **o    *********** ****   * ** * * ** * *o** ***o** 
    ********


OUTPUT SAMPLE:

Print to stdout the minimum number of steps for each test case to get through the labyrinth. If it is impossible to pass the labyrinth — print 0.

For example:

15
0
39

CONSTRAINTS:

Number of test cases is 20.
The length of the cube edge is from 5 to 11.
Moving between levels is 1 step.
There can more than one shortest way.

