# Problem 4: Dutch National Flag Problem
In order to solve this problem in one pass, we use two pointers pointing the start and end of array respectively. If current number is 0, we will swap current number with the number that start pointer points.  (Also be careful with the index, if index < start, index = start.) Otherwise, it would possibly be an infinite loop.
If current number is 1, we add one to index and do nothing. If current number is 2, we swap current number with the number the end pointer points.
Why does this algorithm take O(N) time? The while loop would stop executing when two pointers met. The counter of two pointers also means that we just iterate the array once using two pointers with opposite directions. Therefore, the time complexity depends on the length of the array, and it is linear. In addition, we did not use extra space to store the data. Therefore, the space complexity is O(1).
<br>
**Time complexity: O(N)<br>
Space complexity; O(1)**
