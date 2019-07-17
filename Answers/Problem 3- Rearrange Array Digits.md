# Problem 3: Rearrange Array Digits
In order to meet the requirement for time complexity. I used quicksort to sort
the array. Then, I just construct two lists from the sorted list backwards.
Then I make two numbers based on the two arrays. The reason we do this is because
we always want the left digit of a number to be as big as possible.
Since the quick sort takes N * log(N) time , which dominates in the time complexity.
The time complexity of answer is   N * log(N) + some execution that takes constant time.
Therefore, the overall time complexity is  O(N * logN).

.
