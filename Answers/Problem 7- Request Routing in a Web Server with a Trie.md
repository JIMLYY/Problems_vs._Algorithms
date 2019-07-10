# Problem 7: Request Routing in a Web Server with a Trie
The <insert> and <find> method in class RouteTrie take O(N) complexity where N is the number of components parted by '/' in a path.  Lookup in Route class takes O(N) time as well since it basically just called find method in addition to some O(1) operations.
The space complexity for the Trie is O(M * N). N is the average number of parts of paths in a path, and M is the average  number of unique path components follow a given part. 
