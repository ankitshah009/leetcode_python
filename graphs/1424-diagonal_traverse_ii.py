#1424. Diagonal Traverse II
#Medium
#
#Given a 2D integer array nums, return all elements of nums in diagonal order.
#
#Example 1:
#Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,4,2,7,5,3,8,6,9]
#
#Example 2:
#Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
#Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= nums[i].length <= 10^5
#    1 <= sum(nums[i].length) <= 10^5
#    1 <= nums[i][j] <= 10^5

from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Elements on same diagonal have same (i + j).
        Group by diagonal index, then order by row (descending for each diagonal).
        """
        # Group elements by diagonal (i + j)
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        # Collect result in diagonal order
        # Within each diagonal, elements are added bottom to top
        # (smaller row index comes later in traversal)
        result = []
        for d in range(len(diagonals)):
            # Elements were added top to bottom, we need bottom to top
            result.extend(reversed(diagonals[d]))

        return result


class SolutionReverse:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Process from bottom-right to get correct order"""
        diagonals = defaultdict(list)

        # Process from bottom to top, left to right
        # This naturally gives correct order within diagonal
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        result = []
        d = 0
        while d in diagonals:
            result.extend(diagonals[d])
            d += 1

        return result


class SolutionBFS:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """BFS approach - visit diagonals level by level"""
        from collections import deque

        result = []
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            result.append(nums[r][c])

            # Next diagonal: down (r+1, c) first, then right (r, c+1)
            # This gives correct order within diagonal
            if r + 1 < len(nums) and c < len(nums[r + 1]) and (r + 1, c) not in visited:
                visited.add((r + 1, c))
                queue.append((r + 1, c))

            if c + 1 < len(nums[r]) and (r, c + 1) not in visited:
                visited.add((r, c + 1))
                queue.append((r, c + 1))

        return result


class SolutionTuples:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """Store (diagonal, row, value) and sort"""
        elements = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # Sort by: diagonal index, then row (descending) = -i
                elements.append((i + j, -i, nums[i][j]))

        elements.sort()
        return [val for _, _, val in elements]
