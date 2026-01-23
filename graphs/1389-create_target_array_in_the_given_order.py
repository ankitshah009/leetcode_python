#1389. Create Target Array in the Given Order
#Easy
#
#Given two arrays of integers nums and index. Your task is to create target
#array under the following rules:
#    Initially target array is empty.
#    From left to right read nums[i] and index[i], insert at index index[i]
#    the value nums[i] in target array.
#    Repeat the previous step until there are no elements to read in nums and index.
#
#Return the target array.
#
#It is guaranteed that the insertion operations will be valid.
#
#Example 1:
#Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
#Output: [0,4,1,3,2]
#Explanation:
#nums       index     target
#0            0        [0]
#1            1        [0,1]
#2            2        [0,1,2]
#3            2        [0,1,3,2]
#4            1        [0,4,1,3,2]
#
#Example 2:
#Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
#Output: [0,1,2,3,4]
#
#Example 3:
#Input: nums = [1], index = [0]
#Output: [1]
#
#Constraints:
#    1 <= nums.length, index.length <= 100
#    nums.length == index.length
#    0 <= nums[i] <= 100
#    0 <= index[i] <= i

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Simple simulation using list.insert()
        O(n^2) due to shifting elements on insert
        """
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target


class SolutionExplicit:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """Manual insertion with explicit shifting"""
        target = []

        for i in range(len(nums)):
            idx = index[i]
            num = nums[i]

            # Insert at position idx
            target.append(None)  # Make space

            # Shift elements right
            for j in range(len(target) - 1, idx, -1):
                target[j] = target[j - 1]

            target[idx] = num

        return target


class SolutionLinkedList:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Using linked list concept for O(n) insertions
        (though in Python, list.insert() is simpler)
        """
        class Node:
            def __init__(self, val):
                self.val = val
                self.next = None

        dummy = Node(-1)

        for num, idx in zip(nums, index):
            # Find position to insert
            prev = dummy
            for _ in range(idx):
                prev = prev.next

            # Insert new node
            new_node = Node(num)
            new_node.next = prev.next
            prev.next = new_node

        # Convert to list
        result = []
        curr = dummy.next
        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
