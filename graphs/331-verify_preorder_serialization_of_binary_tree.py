#331. Verify Preorder Serialization of a Binary Tree
#Medium
#
#One way to serialize a binary tree is to use preorder traversal. When we
#encounter a non-null node, we record the node's value. If it is a null node,
#we record using a sentinel value such as '#'.
#
#Given a string of comma-separated values preorder, return true if it is a
#correct preorder traversal serialization of a binary tree.
#
#It is guaranteed that each comma-separated value in the string must be either
#an integer or a character '#' representing null pointer.
#
#Example 1:
#Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
#Output: true
#
#Example 2:
#Input: preorder = "1,#"
#Output: false
#
#Example 3:
#Input: preorder = "9,#,#,1"
#Output: false
#
#Constraints:
#    1 <= preorder.length <= 10^4
#    preorder consist of integers in the range [0, 100] and '#' separated by
#    commas ','.

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        Slot counting approach.
        - Each non-null node consumes 1 slot and produces 2 new slots
        - Each null node consumes 1 slot and produces 0 new slots
        - We start with 1 slot (for root)
        - Valid if slots never go negative and end at 0
        """
        slots = 1
        nodes = preorder.split(',')

        for node in nodes:
            # Consume one slot
            slots -= 1

            # If slots go negative, invalid
            if slots < 0:
                return False

            # Non-null node produces 2 new slots
            if node != '#':
                slots += 2

        return slots == 0


class SolutionStack:
    """Stack-based approach - collapse subtrees"""

    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        nodes = preorder.split(',')

        for node in nodes:
            stack.append(node)

            # Try to collapse: if we see "number, #, #", replace with "#"
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()  # Remove #
                stack.pop()  # Remove #
                stack.pop()  # Remove number
                stack.append('#')  # Collapsed subtree becomes null

        return stack == ['#']


class SolutionDegree:
    """In-degree and out-degree approach"""

    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')

        # diff = out-degree - in-degree
        # Non-null: contributes +1 (out=2, in=1)
        # Null: contributes -1 (out=0, in=1)
        # Root: special case (out=2, in=0)

        diff = 1  # Start with 1 for root's contribution

        for node in nodes:
            diff -= 1  # Consume one in-degree

            if diff < 0:
                return False

            if node != '#':
                diff += 2  # Non-null produces 2 out-degrees

        return diff == 0


class SolutionRecursive:
    """Recursive validation"""

    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        self.index = 0

        def validate():
            if self.index >= len(nodes):
                return False

            if nodes[self.index] == '#':
                self.index += 1
                return True

            self.index += 1  # Move past current node

            # Validate left and right subtrees
            return validate() and validate()

        return validate() and self.index == len(nodes)
