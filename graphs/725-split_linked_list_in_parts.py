#725. Split Linked List in Parts
#Medium
#
#Given the head of a singly linked list and an integer k, split the linked list
#into k consecutive linked list parts.
#
#The length of each part should be as equal as possible: no two parts should
#have a size differing by more than one. This may lead to some parts being null.
#
#The parts should be in the order of occurrence in the input list, and parts
#occurring earlier should always have a size greater than or equal to parts
#occurring later.
#
#Return an array of the k parts.
#
#Example 1:
#Input: head = [1,2,3], k = 5
#Output: [[1],[2],[3],[],[]]
#Explanation: The first element output[0] has output[0].val = 1, output[0].next
#= null. The last element output[4] is null, but its string representation as
#a ListNode is [].
#
#Example 2:
#Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
#Output: [[1,2,3,4],[5,6,7],[8,9,10]]
#Explanation: The input has been split into consecutive parts with size
#difference at most 1, and earlier parts are larger than later ones.
#
#Constraints:
#    The number of nodes in the list is in the range [0, 1000].
#    0 <= Node.val <= 1000
#    1 <= k <= 50

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head, k: int):
        """
        Calculate length, then split into parts of size n//k and n//k+1.
        """
        # Count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Calculate part sizes
        part_size = length // k
        extra = length % k  # First 'extra' parts get one more node

        result = []
        curr = head

        for i in range(k):
            result.append(curr)

            # Size of this part
            size = part_size + (1 if i < extra else 0)

            # Move to end of this part
            for _ in range(size - 1):
                if curr:
                    curr = curr.next

            # Cut the link
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

        return result


class SolutionDetailed:
    """More explicit with edge case handling"""

    def splitListToParts(self, head, k: int):
        # Count nodes
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        # Determine part sizes
        base_size = n // k
        extra = n % k

        result = [None] * k
        curr = head

        for i in range(k):
            if not curr:
                break

            result[i] = curr

            # This part has base_size + 1 if i < extra, else base_size
            part_size = base_size + (1 if i < extra else 0)

            # Traverse to the end of this part
            for _ in range(part_size - 1):
                curr = curr.next

            # Disconnect
            next_head = curr.next
            curr.next = None
            curr = next_head

        return result
