# Problem 3: Rearrange Array Digits
In order to meet the requirement for time complexity. I used quicksort to sort
the array. Then, I just construct two lists from the sorted list backwards.
Then I make two numbers based on the two arrays. The reason we do this is because
we always want the left digit of a number to be as big as possible.

Time complexity for this algorithm is O(N * logN) where logN is time
complexity of quick sort. Space complexity is O(N).
