# Problem 5: Autocomplete with Tries
The time complexity for insert method is O(N) where N is the length of word.
Find method also takes O(N) time complexity because we need to iterate a word to determine whether it can be found.
For suffixes method, the time complexity could be O(M*N) where N is the number of suffixes and
M is the average length of suffixes.
The space complexity for the Trie is O(M ^ N). N is the average number of parts of paths in a path, and M is the average  number of unique path components follow a given part. 
