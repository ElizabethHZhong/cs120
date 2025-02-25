class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    # incorrect - doesn't include right tree in size
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size: 
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    # correct
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    # slow - fix the size calculation
    def insert(self, key):
        if self.key is None:
            self.key = key
            self.size = 1
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
            self.size += 1
        elif self.key < key:
            if self.right is None:
                self.right =                        BinarySearchTree(self.debugger)
            self.right.insert(key)
            self.size += 1
        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if direction == "L":
            if child_side == "L" and self.left:
                self.left = self.left.rotate_left()
            elif self.right:
                self.right = self.right.rotate_left()
        else:
            if child_side == "L" and self.left:
                self.left = self.left.rotate_right()
            elif self.right:
                self.right = self.right.rotate_right()
        return self

    def rotate_left(self):
        temp = BinarySearchTree(self.debugger)
        temp.right = self.right
        if self.right:
            self.size -= self.right.size
            if self.right.left:
                self.size += self.right.left.size
                self.right.size -= self.right.left.size
                self.right = self.right.left
            else:
                self.right = None
            temp.right.left = self
            temp.right.size += self.size
        return temp.right

    def rotate_right(self):
        temp = BinarySearchTree(self.debugger)
        temp.left = self.left
        if self.left:
            self.size -= self.left.size
            if self.left.right:
                self.size += self.left.right.size
                self.left.size -= self.left.right.size
                self.left = self.left.right
            else:
                self.left = None
            temp.left.right = self
            temp.left.size += self.size
        return temp.left

    def calc_size(self):
        if self.left and self.right:
            return self.left.size + self.right.size + 1
        elif self.left and not self.right:
            return self.left.size + 1
        elif not self.left and self.right:
            return self.right.size + 1
        else:
            return 1

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self


def init_tree(key):
    T = BinarySearchTree()
    T.key = key
    return T