== Maximizing Numbers ==

This is the solution to 'Advanced Problem: Maximizing Your Salary'.
The full description of the problem can be found on Algo -Maximizing Numbers >
Problem Description > Advanced - Maximizing Your Salary

In short, we are required to form a largest number possible from several input of
numbers. For example, we may want our solution to output 221 instead of 212
when the inputs are 21 and 2. Similarly, our solution should output 979797
instead of 797799 when the inputs are 797, 79, and 9.

There are ways to approach this problem. There are 3 solutions presented in this
project: the suggested original solution, suggested original solution
with sort and group functions, and digits scoring. The scripts (written in Python)
of these 3 solutions can be found in Algo - Maximizing Numbers > Source Code

The strategy used in the suggested original solution is:
1. Turn number X into string
2. Turn number Y into string
3. Compare XY and YX
4. If XY > YX, return X, append X to the formed_number_list, and remove X from
the input_number_list

Since 5 will always be placed in earlier sequence if compared with 4, 49, or 499
but will not always be placed in earlier sequence if compared with 51, 55, or 59,
therefore we only need to evaluate 5 with other numbers that begin with "5", similarly
we only need to evaluate 4 with other numbers that begin with "4".

Therefore we can improve the original suggested solution by sorting and grouping
the numbers and putting them into a dictionary before evaluating them.

{9 : [998, 92, 91, 9]}
{8 : [894, 86, 81, 8]}
{.
.
.
{1 : [198, 18, 17, 1]}

By doing so, with 10,000 numbers being inputted we do not need to evaluate 1 number against
the other 9,999 numbers thus reducing the running time significantly. 90 seconds vs 10 seconds
on 10,000 inputs with numbers' string ranging from 1 - 999.

However, there are faster solution than comparing 2 numbers which I wrote, I named it as
"Digits Scoring". The idea is to compare the score of each number.  

If we compare 5 against 59, we should place 59 first before 5. However, if we compare
5 against 51, 5 should be in the earlier sequence than 51. If we look closely, we
may realize when we sum the digits and divide them by the their length we will get the
score that correspond to our logic.

Since score = ( sum of the digits / length of the digits). Therefore, { number:score }
will be { 59:7, 5:5, 51:3 } thus 59 will be placed earlier than 5 and 5 will be placed earlier than 51.

However, if we compare 3 digits numbers such as 529 vs 531 with the same method, we will get the wrong
answer since { 529:5.3 , 531:3 }. Therefore, we may not want to put the third digit into our score
calculation. The solution to this is to only score the first second digits of the number and compensate
the last digit of the number with compensation. Put it another way, we only take 52 in number 529 and 53
in number 531 thus will produce { 531 : 4 + compensation, 529 : 3.5 + compensation}. But how large
the compensation should be?

Since we may want to compensate the score fairly, if we look 514 vs 51 and 516 vs 51.
we need to put 516 first before 51 but 51 first before 514. Therefore, when the value of
the last digit is higher than the first digit, we will give the number bigger compensation,
and when the value of the last digit is lower than the first digit we will give the number
smaller compensation.

Therefore, compensation_third = (first digit - third digit) / 100

However, if we evaluate 545 vs 54 and 565 vs 56, we may find that
54 will be first and 545 second but 565 will be the first and 56 second.
Therefore we need to compensate the second digit as well but instead of bring
the compensation to a hundredth, we bring the number to a tenth. Thus we can write
the compensation for the second digit as follow:

compensation_second = (first digit - second digit) / 10

By scoring the numbers, sorting, and grouping them according to their score
we can reduce the running time way significantly than the previous method. 0.2
seconds vs 10 seconds on 10,000 inputs with numbers' string ranging from 1 - 999

To test the three methods, please navigate to Algo - Maximizing Numbers > Standalone
Applications (Windows Only), download all the files and move them to a designated location
in your system. Please do note that the program will read 'numbers.txt' in the same folder
where the program is located.

To change the input in numbers.txt
1. Please generate random numbers from https://andrew.hedges.name/experiments/random/
2. Select all (CTRL+A) and copy (CTRL+C)
3. Open 'numbers.txt', select all (CTRL+A), paste (CTRL+V), and save (CTRL+S)

Since the rule for numbers larger than 3 digits has not been written in the script.
Please do note that digits_scoring.exe can only evaluate up to 3 digits.

The sample result of the program could be found on Algo - Maximizing Numbers > Sample Result

Thank you for reading
Have a nice day,
Fernandi

January 2018
