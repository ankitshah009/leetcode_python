#817. Linked List Components
#Medium
#
#You are given the head of a linked list containing unique integer values and
#an integer array nums that is a subset of the linked list values.
#
#Return the number of connected components in nums where two values are
#connected if they appear consecutively in the linked list.
#
#Example 1:
#Input: head = [0,1,2,3], nums = [0,1,3]
#Output: 2
#Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
#
#Example 2:
#Input: head = [0,1,2,3,4], nums = [0,3,1,4]
#Output: 2
#Explanation: 0 and 1 are connected, 3 and 4 are connected.
#
#Constraints:
#    The number of nodes in the linked list is n.
#    1 <= n <= 10^4
#    0 <= Node.val < n
#    All the values Node.val are unique.
#    1 <= nums.length <= n
#    0 <= nums[i] < n
#    All the values of nums are unique.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        """
        Count transitions from 'in nums' to 'not in nums' or end of list.
        Each such transition marks the end of a component.
        """
        nums_set = set(nums)
        count = 0
        in_component = False

        current = head
        while current:
            if current.val in nums_set:
                in_component = True
            else:
                if in_component:
                    count += 1
                    in_component = False
            current = current.next

        # Don't forget the last component
        if in_component:
            count += 1

        return count


class SolutionSimple:
    """Simpler: count component starts"""

    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        nums_set = set(nums)
        count = 0

        current = head
        while current:
            if current.val in nums_set:
                # Check if this is start of new component
                if not current.next or current.next.val not in nums_set:
                    count += 1
            current = current.next

        return count


class SolutionAlternative:
    """Count component starts instead of ends"""

    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        nums_set = set(nums)
        count = 0
        prev_in = False

        current = head
        while current:
            curr_in = current.val in nums_set
            if curr_in and not prev_in:
                count += 1
            prev_in = curr_in
            current = current.next

        return count
