#160. Intersection of Two Linked Lists
#Easy
#
#Given the heads of two singly linked-lists headA and headB, return the node at which the
#two lists intersect. If the two linked lists have no intersection at all, return null.
#
#Example 1:
#Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
#Output: Intersected at '8'
#
#Example 2:
#Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
#Output: Intersected at '2'
#
#Example 3:
#Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
#Output: No intersection
#
#Constraints:
#    The number of nodes of listA is in the m.
#    The number of nodes of listB is in the n.
#    1 <= m, n <= 3 * 10^4
#    1 <= Node.val <= 10^5
#    0 <= skipA < m
#    0 <= skipB < n
#    intersectVal is 0 if listA and listB do not intersect.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
