# Problem 2: Search in a Rotated Sorted Array
This is a binary search question. mid is the midpoint of left and right. If input_list[mid] < input_list[right], it means that midpoint is in right part of the array (segmented by rotated center). Furthermore， If "input_list[mid] < number <= input_list[right]" is right, we can move the left to mid + 1. Otherwise, we move right to mid - 1.

On the contrary, if "input_list[mid] < input_list[right]", it means that midpoint is in left part of the array (segmented by rotated center). Similarly, we check again input_list[left] <= number < input_list[mid] to determine how to deal with left and right.<br>

Binary search is a search algorithms where we find the position of a target value by comparing the
mid value with this target value. If the mid value is equal to the target value, then we find the answer. Otherwise, if the target value comes before the mid value, we look for the target value in the left half. If the target value comes after the middle value, we look for the value in the right half. We then repeat this process as many as needed, until we find the target value (if it is exists). As we can see, when we compare the mid value with target and determine which half we should go to, we actually discard another half. As we repeat this over and over again, we can know that the time complexity is O(log(N)). The space complexity is O(1) since we only used the constant space. 

**Time complexity: O(log N)<br>
Space complexity; O(1)**
