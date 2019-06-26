# Problem 2: Search in a Rotated Sorted Array
This is a binary search question. mid is the midpoint of left and right. If input_list[mid] < input_list[right], it means that midpoint is in right part of the array (segmented by rotated center). Furthermore， If "input_list[mid] < number <= input_list[right]" is right, we can move the left to mid + 1. Otherwise, we move right to mid - 1.

On the contrary, if "input_list[mid] < input_list[right]", it means that midpoint is in left part of the array (segmented by rotated center). Similarly, we check again input_list[left] <= number < input_list[mid] to determine how to deal with left and right.<br>

** Time complexity: O(log N)<br>
Space complexity; O(1) **
