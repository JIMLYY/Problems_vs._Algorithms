# Problem 1: Square Root of an Integer
**Explanation**: The question requires a O(log(N)) time complexity, which naturally remind us of using binary search to tackle this problem.
First of all, we handle the corner case where the given number is 0 by simply returning 0.
Then we conducted binary search step by step by using a while loop. The exit is when mid ^ 2 <= number and (mid + 1) ^ 2 > number.<br>
Why does binary search have time complexity of log(N)?
Let's take a look at how binary search works. Basically, binary search is a search algorithms where we find the position of a target value by comparing the
middle value with this target value. If the middle value is equal to the target
value, then we find the answer. Otherwise, if the target value comes before the
middle value, we look for the target value in the left half. If the target value comes after the middle value, we look for the value in the right half. We
then repeat this process as many as needed, until we find the target value (if it is exists). As we can see, when we compare the middle value with target and determine which half we should go to, we actually discard another half. As we repeat this over and over again, we can know that the time complexity is O(log(N)). Additionally, we only used the constant space. Therefore, the space complexity should be O(1). 

**Time complexity : O(log(N)) <br>
Space complexity: O(1)**
