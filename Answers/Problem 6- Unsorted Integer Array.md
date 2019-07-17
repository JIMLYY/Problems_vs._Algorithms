# Problem 6: Unsorted Integer Array
This is a simple question. First of all, we need to define two variables to store the max value and min value respectively. Then, all we need to do is traversing the array while compare each number with maxVal and minVal. If the number is greater than maxVal, the val will be assigned to maxVal. If the number is less than minVal, the value will be assigned to minVal. Since we just iterate the array one time, and constant operation would be executed each iteration. Therefore, the time complexity is O(N).
Also, we did not take extra space in this algorithms. Therefore, the space complexity is O(1).
**Time complexity: O(N)<br>
Space complexity; O(1)**
