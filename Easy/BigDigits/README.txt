Big Digits
Challenge Description:

Sometimes, there is a need to output big symbols on the devices, which support only ASCII characters and single fixed-width fonts. The only way to do this is to use the pseudographics for drawing big symbols.

Here is an example of the font with digits from 0 to 9:

Each pixel is marked either with asterisk ‘*’ or with minus ‘-’. Size of a digit is 5×6 pixels.

Your task is to write a program, which outputs the numbers given to you with the font as in the example.
Input sample:

3.1415926
1.41421356
01-01-1970
2.7182818284
4 8 15 16 23 42

The first argument is a file that contains the lines with digits sequences you need to magnify. E.g.:
Output sample:

Print to stdout the magnified digits:

***----*---*-----*--****--**--***---**--
---*--**--*--*--**--*----*--*----*-*----
-**----*--****---*--***---***--**--***--
---*---*-----*---*-----*----*-*----*--*-
***---***----*--***-***---**--****--**--
----------------------------------------
--*---*-----*---*---***----*--***--****--**--
-**--*--*--**--*--*----*--**-----*-*----*----
--*--****---*--****--**----*---**--***--***--
--*-----*---*-----*-*------*-----*----*-*--*-
-***----*--***----*-****--***-***--***---**--
---------------------------------------------
-**----*---**----*----*---**--****--**--
*--*--**--*--*--**---**--*--*----*-*--*-
*--*---*--*--*---*----*---***---*--*--*-
*--*---*--*--*---*----*-----*--*---*--*-
-**---***--**---***--***--**---*----**--
----------------------------------------
***--****---*---**--***---**----*---**--***---**---*---
---*----*--**--*--*----*-*--*--**--*--*----*-*--*-*--*-
-**----*----*---**---**---**----*---**---**---**--****-
*-----*-----*--*--*-*----*--*---*--*--*-*----*--*----*-
****--*----***--**--****--**---***--**--****--**-----*-
-------------------------------------------------------
-*----**----*--****---*---**--***--***---*---***--
*--*-*--*--**--*-----**--*-------*----*-*--*----*-
****--**----*--***----*--***---**---**--****--**--
---*-*--*---*-----*---*--*--*-*-------*----*-*----
---*--**---***-***---***--**--****-***-----*-****-
--------------------------------------------------

Constraints:

    Input lines are up to 16 symbols long.
    Input can contain some other symbols, which should be ignored (i.e. points, hyphens, spaces); only numbers must be printed out.

