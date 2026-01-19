#237. Delete Node in a Linked List
#Medium
#
#There is a singly-linked list head and we want to delete a node node in it.
#
#You are given the node to be deleted node. You will not be given access to the
#first node of head.
#
#All the values of the linked list are unique, and it is guaranteed that the
#given node node is not the last node in the linked list.
#
#Delete the given node. Note that by deleting the node, we do not mean removing
#it from memory. We mean:
#    The value of the given node should not exist in the linked list.
#    The number of nodes in the linked list should decrease by one.
#    All the values before node should be in the same order.
#    All the values after node should be in the same order.
#
#Example 1:
#Input: head = [4,5,1,9], node = 5
#Output: [4,1,9]
#Explanation: You are given the second node with value 5, the linked list should
#become 4 -> 1 -> 9 after calling your function.
#
#Example 2:
#Input: head = [4,5,1,9], node = 1
#Output: [4,5,9]
#Explanation: You are given the third node with value 1, the linked list should
#become 4 -> 5 -> 9 after calling your function.
#
#Constraints:
#    The number of the nodes in the given list is in the range [2, 1000].
#    -1000 <= Node.val <= 1000
#    The value of each node in the list is unique.
#    The node to be deleted is in the list and is not a tail node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Since we don't have access to the previous node, we can't delete the
        current node directly. Instead, we copy the value from the next node
        and delete the next node.
        """
        # Copy value from next node
        node.val = node.next.val

        # Skip the next node (effectively deleting it)
        node.next = node.next.next


class SolutionVerbose:
    """Same solution with more explicit steps"""

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Get the next node
        next_node = node.next

        # Copy the value
        node.val = next_node.val

        # Update the pointer to skip next_node
        node.next = next_node.next

        # next_node is now orphaned and will be garbage collected


# Note: This is a bit of a trick question. The standard way to delete a node
# from a linked list requires access to the previous node. Since we don't have
# that, we use this "copy and delete next" trick instead.
#
# Limitations of this approach:
# 1. Cannot delete the last node (constraint says it won't be given)
# 2. If nodes have references elsewhere, those references will point to wrong node
# 3. If node values are complex objects, copying might be expensive
