#708. Insert into a Sorted Circular Linked List
#Medium
#
#Given a Circular Linked List node, which is sorted in non-descending order,
#write a function to insert a value insertVal into the list such that it
#remains a sorted circular list. The given node can be a reference to any
#single node in the list and may not necessarily be the smallest value in
#the circular list.
#
#If there are multiple suitable places for insertion, you may choose any place
#to insert the new value. After the insertion, the circular list should remain
#sorted.
#
#If the list is empty (i.e., the given node is null), you should create a new
#single circular list and return the reference to that single node. Otherwise,
#you should return the originally given node.
#
#Example 1:
#Input: head = [3,4,1], insertVal = 2
#Output: [3,4,1,2]
#Explanation: In the figure above, there is a sorted circular list of three
#elements. You are given a reference to the node with value 3, and we need to
#insert 2 into the list. The new node should be inserted between node 1 and
#node 3. After the insertion, the list becomes [3,4,1,2].
#
#Example 2:
#Input: head = [], insertVal = 1
#Output: [1]
#Explanation: The list is empty (given head is null). We create a new single
#circular list and return the reference to that single node.
#
#Example 3:
#Input: head = [1], insertVal = 0
#Output: [1,0]
#
#Constraints:
#    The number of nodes in the list is in the range [0, 5 * 10^4].
#    -10^6 <= Node.val, insertVal <= 10^6

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insert(self, head, insertVal: int):
        """
        Three cases:
        1. Normal case: prev.val <= insertVal <= curr.val
        2. At tail: insertVal is max/min (at the wrap-around point)
        3. All same values: insert anywhere after full traversal
        """
        new_node = Node(insertVal)

        # Empty list
        if not head:
            new_node.next = new_node
            return new_node

        prev, curr = head, head.next

        while True:
            # Case 1: Normal insert position
            if prev.val <= insertVal <= curr.val:
                break

            # Case 2: At the tail (wrap-around point)
            if prev.val > curr.val:
                # Insert if it's the new max or min
                if insertVal >= prev.val or insertVal <= curr.val:
                    break

            prev = curr
            curr = curr.next

            # Case 3: Completed full loop (all same values)
            if prev == head:
                break

        prev.next = new_node
        new_node.next = curr

        return head


class SolutionDetailed:
    """More explicit handling of edge cases"""

    def insert(self, head, insertVal: int):
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        # Single node
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head

        # Find insertion point
        prev = head
        curr = head.next

        while True:
            # Found correct position in sorted part
            if prev.val <= insertVal <= curr.val:
                break

            # At the boundary (max to min transition)
            if prev.val > curr.val:
                if insertVal >= prev.val:  # New max
                    break
                if insertVal <= curr.val:  # New min
                    break

            prev = curr
            curr = curr.next

            # Back to start - insert anywhere (all same or went full circle)
            if prev == head:
                break

        # Insert between prev and curr
        prev.next = new_node
        new_node.next = curr

        return head
