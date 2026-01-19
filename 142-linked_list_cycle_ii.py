#142. Linked List Cycle II
#Medium
#
#Given the head of a linked list, return the node where the cycle begins. If there is no cycle,
#return null.
#
#Example 1:
#Input: head = [3,2,0,-4], pos = 1
#Output: tail connects to node index 1
#Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#Example 2:
#Input: head = [1,2], pos = 0
#Output: tail connects to node index 0
#
#Example 3:
#Input: head = [1], pos = -1
#Output: no cycle
#
#Constraints:
#    The number of the nodes in the list is in the range [0, 10^4].
#    -10^5 <= Node.val <= 10^5
#    pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = fast = head

        # Find meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # Find cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
