#1306. Jump Game III
#Medium
#
#Given an array of non-negative integers arr, you are initially positioned at
#start index of the array. When you are at index i, you can jump to i + arr[i]
#or i - arr[i], check if you can reach to any index with value 0.
#
#Notice that you can not jump outside of the array at any time.
#
#Example 1:
#Input: arr = [4,2,3,0,3,1,2], start = 5
#Output: true
#Explanation:
#All possible ways to reach at index 3 with value 0 are:
#index 5 -> index 4 -> index 1 -> index 3
#index 5 -> index 6 -> index 4 -> index 1 -> index 3
#
#Example 2:
#Input: arr = [4,2,3,0,3,1,2], start = 0
#Output: true
#Explanation:
#One possible way to reach at index 3 with value 0 is:
#index 0 -> index 4 -> index 1 -> index 3
#
#Example 3:
#Input: arr = [3,0,2,1,2], start = 2
#Output: false
#Explanation: There is no way to reach at index 1 with value 0.
#
#Constraints:
#    1 <= arr.length <= 5 * 10^4
#    0 <= arr[i] < arr.length
#    0 <= start < arr.length

from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """BFS to find if we can reach index with value 0."""
        n = len(arr)
        visited = set()
        queue = deque([start])

        while queue:
            idx = queue.popleft()

            if arr[idx] == 0:
                return True

            if idx in visited:
                continue
            visited.add(idx)

            # Try both jumps
            for next_idx in [idx + arr[idx], idx - arr[idx]]:
                if 0 <= next_idx < n and next_idx not in visited:
                    queue.append(next_idx)

        return False


class SolutionDFS:
    def canReach(self, arr: List[int], start: int) -> bool:
        """DFS recursive solution"""
        n = len(arr)
        visited = set()

        def dfs(idx):
            if idx < 0 or idx >= n or idx in visited:
                return False

            if arr[idx] == 0:
                return True

            visited.add(idx)
            return dfs(idx + arr[idx]) or dfs(idx - arr[idx])

        return dfs(start)


class SolutionMarkVisited:
    def canReach(self, arr: List[int], start: int) -> bool:
        """Mark visited by negating values (modifies input)"""
        n = len(arr)

        def dfs(idx):
            if idx < 0 or idx >= n or arr[idx] < 0:
                return False

            if arr[idx] == 0:
                return True

            jump = arr[idx]
            arr[idx] = -1  # Mark as visited

            return dfs(idx + jump) or dfs(idx - jump)

        return dfs(start)
