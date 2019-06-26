# Problem 1: Square Root of an Integer
** Explanation **: The question requires a O(log(N)) time complexity, which naturally remind us of using binary search to tackle this problem.
First of all, we handle the corner case where the given number is 0 by simply returning 0.
Then we conducted binary search step by step by using a while loop. The exit is when mid ^ 2 <= number and (mid + 1) ^ 2 > number.<br>
** Time complexity : O(log(N)) <br>
Space complexity: O(1) **
