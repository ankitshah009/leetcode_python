#173. Binary Search Tree Iterator
#Medium
#
#Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
#    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#    int next() Moves the pointer to the right, then returns the number at the pointer.
#
#Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
#You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
#
# 
#
#Example 1:
#
#Input
#["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
#[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
#Output
#[null, 3, 7, true, 9, true, 15, true, 20, false]
#
#Explanation
#BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
#bSTIterator.next();    // return 3
#bSTIterator.next();    // return 7
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 9
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 15
#bSTIterator.hasNext(); // return True
#bSTIterator.next();    // return 20
#bSTIterator.hasNext(); // return False
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is in the range [1, 105].
#    0 <= Node.val <= 106
#    At most 105 calls will be made to hasNext, and next.
#
# 
#
#Follow up:
#
#    Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes_sorted=[]
        self.index=-1
        self._inorder(root)
        
    def _inorder(self,root):
        if not root:
            return 
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)
        
    def next(self) -> int:
        self.index+=1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        return self.index +1 <len(self.nodes_sorted)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """

        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0
