#255. Verify Preorder Sequence in Binary Search Tree
#Medium
#
#Given an array of unique integers preorder, return true if it is the correct
#preorder traversal sequence of a binary search tree.
#
#Example 1:
#Input: preorder = [5,2,1,3,6]
#Output: true
#
#Example 2:
#Input: preorder = [5,2,6,1,3]
#Output: false
#
#Constraints:
#    1 <= preorder.length <= 10^4
#    1 <= preorder[i] <= 10^4
#    All the elements of preorder are unique.
#
#Follow up: Could you do it using only constant space complexity?

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Use monotonic stack approach
        # Track lower bound for valid values
        stack = []
        lower_bound = float('-inf')

        for val in preorder:
            # If current value is less than lower bound, invalid
            if val < lower_bound:
                return False

            # Pop from stack while current is greater than stack top
            # This means we're moving to right subtree
            while stack and val > stack[-1]:
                lower_bound = stack.pop()

            stack.append(val)

        return True

    # O(1) space: modify input array as stack
    def verifyPreorderConstantSpace(self, preorder: List[int]) -> bool:
        lower_bound = float('-inf')
        stack_idx = -1

        for val in preorder:
            if val < lower_bound:
                return False

            while stack_idx >= 0 and val > preorder[stack_idx]:
                lower_bound = preorder[stack_idx]
                stack_idx -= 1

            stack_idx += 1
            preorder[stack_idx] = val

        return True

    # Recursive approach with bounds
    def verifyPreorderRecursive(self, preorder: List[int]) -> bool:
        self.idx = 0

        def helper(min_val, max_val):
            if self.idx >= len(preorder):
                return True

            val = preorder[self.idx]
            if val < min_val or val > max_val:
                return False

            self.idx += 1

            # Try to build left subtree, then right subtree
            # Left subtree: values between (min_val, val)
            # Right subtree: values between (val, max_val)
            return helper(min_val, val) or helper(val, max_val)

        return helper(float('-inf'), float('inf')) and self.idx == len(preorder)
