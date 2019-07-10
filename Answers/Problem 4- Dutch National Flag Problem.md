# Problem 4: Dutch National Flag Problem
In order to solve this problem in one pass, we use two pointers pointing the start and end of array respectively. If current number is 0, we will swap current number with the number that start pointer points.  Also be careful with the index, if index < start, index = start. Otherwise, it would possibly be an infinite loop.
If current number is 1, we add one to index and do nothing. If current number is 2, we swap current number with the number the end pointer points.
<br>
**Time complexity: O(log N)<br>
Space complexity; O(1)**
