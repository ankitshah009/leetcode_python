#1580. Put Boxes Into the Warehouse II
#Medium
#
#You are given two arrays of positive integers, boxes and warehouse, representing
#the heights of some boxes of unit width and the heights of n rooms in a warehouse
#respectively. The warehouse's rooms are labeled from 0 to n - 1 from left to
#right where warehouse[i] (0-indexed) is the height of the ith room.
#
#Boxes are put into the warehouse by the following rules:
#- Boxes cannot be stacked.
#- You can rearrange the insertion order of the boxes.
#- Boxes can be pushed into the warehouse from either side (left or right).
#- If the height of some room in the warehouse is less than the height of a box,
#  then that box and all other boxes behind it will be stopped before that room.
#
#Return the maximum number of boxes you can put into the warehouse.
#
#Example 1:
#Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
#Output: 4
#Explanation: We can store the boxes in the following order:
#1- Put the yellow box in room 2 from the left side.
#2- Put the orange box in room 3 from the right side.
#3- Put the green box in room 1 from the left side.
#4- Put the red box in room 0 from the left side.
#
#Example 2:
#Input: boxes = [3,5,5,2], warehouse = [2,1,3,4,5]
#Output: 3
#
#Constraints:
#    n == warehouse.length
#    1 <= boxes.length, warehouse.length <= 10^5
#    1 <= boxes[i], warehouse[i] <= 10^9

from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Since we can push from either side, each room's effective height
        is the max of: min from left and min from right.

        Then greedily match sorted boxes to sorted room heights.
        """
        n = len(warehouse)

        # Calculate effective height from left
        left_min = [0] * n
        left_min[0] = warehouse[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], warehouse[i])

        # Calculate effective height from right
        right_min = [0] * n
        right_min[n - 1] = warehouse[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], warehouse[i])

        # Effective height is max of left and right access
        effective = [max(left_min[i], right_min[i]) for i in range(n)]

        # Sort both boxes and effective heights
        boxes.sort()
        effective.sort()

        # Greedily match smallest boxes to smallest rooms
        count = 0
        j = 0  # pointer for effective heights

        for box in boxes:
            while j < n and effective[j] < box:
                j += 1
            if j >= n:
                break
            count += 1
            j += 1

        return count


class SolutionTwoPointers:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Two pointers on warehouse: push from left or right.
        Sort boxes descending and try to place largest first.
        """
        boxes.sort(reverse=True)
        n = len(warehouse)
        left, right = 0, n - 1
        count = 0

        for box in boxes:
            if left > right:
                break

            if warehouse[left] >= box:
                # Can push from left
                count += 1
                left += 1
            elif warehouse[right] >= box:
                # Can push from right
                count += 1
                right -= 1
            else:
                # Box too tall, but it limits the effective height
                # from whichever side is shorter
                if warehouse[left] < warehouse[right]:
                    # Left is the bottleneck, shrink from left
                    left += 1
                else:
                    right -= 1

        return count


class SolutionEffective:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Calculate effective heights considering both directions.
        """
        n = len(warehouse)

        # Effective height from left
        eff_left = warehouse.copy()
        for i in range(1, n):
            eff_left[i] = min(eff_left[i - 1], warehouse[i])

        # Effective height from right
        eff_right = warehouse.copy()
        for i in range(n - 2, -1, -1):
            eff_right[i] = min(eff_right[i + 1], warehouse[i])

        # Best effective height per room
        effective = [max(eff_left[i], eff_right[i]) for i in range(n)]

        # Sort and match
        boxes.sort()
        effective.sort()

        bi = 0
        for height in effective:
            if bi < len(boxes) and boxes[bi] <= height:
                bi += 1

        return bi
