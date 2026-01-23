#1564. Put Boxes Into the Warehouse I
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
#- Boxes can only be pushed into the warehouse from left to right only.
#- If the height of some room in the warehouse is less than the height of a box,
#  then that box and all other boxes behind it will be stopped before that room.
#
#Return the maximum number of boxes you can put into the warehouse.
#
#Example 1:
#Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
#Output: 3
#Explanation: We can place the 3 boxes as shown: [4,3,1] in rooms [0,1,4].
#The box of height 4 goes to room 0, box of height 3 goes to room 1, and box
#of height 1 goes to room 4.
#We cannot put boxes 0 and 2 as their heights exceed room heights at some point.
#
#Example 2:
#Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
#Output: 3
#Explanation: Notice that it's not possible to put box 4 into the warehouse
#since it cannot pass through room 2 (height 1).
#Also, for the last 2 rooms, 2 and 3, only boxes of height 1 can fit.
#We can place 3 boxes: [2,1,1] in rooms [0,2,3].
#
#Example 3:
#Input: boxes = [1,2,3], warehouse = [1,2,3,4]
#Output: 1
#Explanation: Since room 0 has height 1, only box 0 of height 1 can go inside.
#
#Constraints:
#    n == warehouse.length
#    1 <= boxes.length, warehouse.length <= 10^5
#    1 <= boxes[i], warehouse[i] <= 10^9

from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Key insight: Boxes must enter from left. Room i is limited by
        min(warehouse[0], ..., warehouse[i]).

        Strategy:
        1. Calculate effective heights for each room
        2. Sort boxes in ascending order
        3. Greedily place smallest boxes in rightmost available rooms
        """
        n = len(warehouse)

        # Calculate effective height for each room (limited by minimum to the left)
        effective = [0] * n
        effective[0] = warehouse[0]
        for i in range(1, n):
            effective[i] = min(effective[i - 1], warehouse[i])

        # Sort boxes (ascending) and effective heights (descending by position)
        boxes.sort()

        count = 0
        box_idx = 0

        # Try to place boxes from rightmost room (which has lowest effective height)
        for room in range(n - 1, -1, -1):
            if box_idx >= len(boxes):
                break

            if boxes[box_idx] <= effective[room]:
                count += 1
                box_idx += 1

        return count


class SolutionTwoPointers:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Two pointer approach: sort boxes descending, try to place from left.
        """
        boxes.sort(reverse=True)

        count = 0
        box_idx = 0
        min_height = float('inf')

        for height in warehouse:
            min_height = min(min_height, height)

            # Skip boxes that are too tall
            while box_idx < len(boxes) and boxes[box_idx] > min_height:
                box_idx += 1

            if box_idx >= len(boxes):
                break

            # Place this box
            count += 1
            box_idx += 1

        return count


class SolutionOptimized:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Optimized: Process rooms and boxes together.
        """
        # Precompute effective heights
        n = len(warehouse)
        effective = warehouse.copy()
        for i in range(1, n):
            effective[i] = min(effective[i], effective[i - 1])

        # Sort boxes ascending
        boxes.sort()

        # Two pointers: smallest box with rightmost room
        placed = 0
        room = n - 1

        for box in boxes:
            # Find rightmost room that can fit this box
            while room >= 0 and effective[room] < box:
                room -= 1

            if room < 0:
                break

            placed += 1
            room -= 1

        return placed


class SolutionGreedy:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        """
        Greedy with explicit simulation.
        """
        # Calculate limiting heights
        n = len(warehouse)
        limits = [0] * n
        limits[0] = warehouse[0]
        for i in range(1, n):
            limits[i] = min(limits[i - 1], warehouse[i])

        # Sort boxes ascending
        boxes_sorted = sorted(boxes)

        # Place smallest boxes first, from back of warehouse
        placed = 0
        j = len(boxes_sorted) - 1

        for i in range(n):
            # Current room has limit limits[i]
            pass

        # Alternative: sort rooms by effective height and greedily match
        room_heights = sorted(enumerate(limits), key=lambda x: x[1])
        boxes_sorted = sorted(boxes)

        bi = 0
        for _, height in room_heights:
            if bi < len(boxes_sorted) and boxes_sorted[bi] <= height:
                placed += 1
                bi += 1

        return placed
