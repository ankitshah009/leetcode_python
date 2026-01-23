#889. Construct Binary Tree from Preorder and Postorder Traversal
#Medium
#
#Given two integer arrays, preorder and postorder where preorder is the preorder
#traversal of a binary tree of distinct values and postorder is the postorder
#traversal of the same tree, reconstruct and return the binary tree.
#
#If there exist multiple answers, you can return any of them.
#
#Example 1:
#Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
#Output: [1,2,3,4,5,6,7]
#
#Example 2:
#Input: preorder = [1], postorder = [1]
#Output: [1]
#
#Constraints:
#    1 <= preorder.length <= 30
#    1 <= preorder[i] <= preorder.length
#    All the values of preorder are unique.
#    postorder.length == preorder.length
#    1 <= postorder[i] <= postorder.length
#    All the values of postorder are unique.
#    It is guaranteed that preorder and postorder are the preorder and postorder
#    traversals of the same binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        """
        preorder: [root, left_subtree, right_subtree]
        postorder: [left_subtree, right_subtree, root]

        First element of preorder is root.
        Second element of preorder (if exists) is root of left subtree.
        Find this in postorder to determine left subtree size.
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        # Left subtree root is preorder[1]
        left_root_val = preorder[1]
        # Find it in postorder to get left subtree size
        left_size = postorder.index(left_root_val) + 1

        root.left = self.constructFromPrePost(
            preorder[1:1+left_size],
            postorder[:left_size]
        )
        root.right = self.constructFromPrePost(
            preorder[1+left_size:],
            postorder[left_size:-1]
        )

        return root


class SolutionIterative:
    """Iterative with stack"""

    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        post_idx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            while stack[-1].val == postorder[post_idx]:
                stack.pop()
                post_idx += 1

            if stack[-1].left is None:
                stack[-1].left = node
            else:
                stack[-1].right = node

            stack.append(node)

        return root


class SolutionIndex:
    """Using index lookup for efficiency"""

    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        post_index = {v: i for i, v in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])

            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]
            left_size = post_index[left_root_val] - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_size,
                             post_start, post_start + left_size - 1)
            root.right = build(pre_start + left_size + 1, pre_end,
                              post_start + left_size, post_end - 1)

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
