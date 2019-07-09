# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        
    def insert(self, path, handler):
        # Recursively add nodes
        curr_node = self.root
        for component in path:
            curr_node = curr_node.children[component]
        # Assign the handler to only the leaf (deepest) node of this path    
        curr_node.handler = handler
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        curr_node = self.root
        for component in path:
            if component not in curr_node.children:
                return None
            curr_node = curr_node.children[component]
        # Return the handler for a match, or None for no match    
        return curr_node.handler
    
# Define RouteTrieNode class with children and handler elements 
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        import collections 
        self.children = collections.defaultdict(RouteTrieNode)
        self.handler = handler
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(handler)
        # Add a handler for 404 page not found responses 
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        path_parts = Router.split_path(path)
        self.trie.insert(path_parts, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # else return the "not found" handler 
        path_parts = Router.split_path(path)
        handler = self.trie.find(path_parts)
        if handler:
            return handler
        else:
            return self.not_found_handler
        

    def split_path(path):
        # Split the path into parts  
        res = []
        parted_path = path.split("/")
        for part in parted_path:
            if part:
                res += [part]
        return res
        




# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# reference: @ Eric Melz 's repository https://github.com/ericmelz/DSND.git
