#1345. Jump Game IV
#Hard
#
#Given an array of integers arr, you are initially positioned at the first
#index of the array.
#
#In one step you can jump from index i to index:
#    i + 1 where: i + 1 < arr.length.
#    i - 1 where: i - 1 >= 0.
#    j where: arr[i] == arr[j] and i != j.
#
#Return the minimum number of steps to reach the last index of the array.
#
#Notice that you can not jump outside of the array at any time.
#
#Example 1:
#Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
#Output: 3
#Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
#
#Example 2:
#Input: arr = [7]
#Output: 0
#Explanation: Start index is the last index. You do not need to jump.
#
#Example 3:
#Input: arr = [7,6,9,6,9,6,9,7]
#Output: 1
#Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
#
#Constraints:
#    1 <= arr.length <= 5 * 10^4
#    -10^8 <= arr[i] <= 10^8

from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        BFS with optimization: after using all indices with same value,
        remove them from the map to avoid revisiting.
        """
        n = len(arr)
        if n == 1:
            return 0

        # Group indices by value
        value_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_indices[val].append(i)

        # BFS
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                idx = queue.popleft()

                # Jump to same value indices
                for j in value_indices[arr[idx]]:
                    if not visited[j]:
                        if j == n - 1:
                            return steps
                        visited[j] = True
                        queue.append(j)

                # Clear to avoid revisiting same-value indices
                value_indices[arr[idx]].clear()

                # Jump to neighbors
                for j in [idx - 1, idx + 1]:
                    if 0 <= j < n and not visited[j]:
                        if j == n - 1:
                            return steps
                        visited[j] = True
                        queue.append(j)

        return -1


class SolutionBidirectional:
    def minJumps(self, arr: List[int]) -> int:
        """Bidirectional BFS for potentially faster search"""
        n = len(arr)
        if n == 1:
            return 0

        # Group indices by value
        value_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_indices[val].append(i)

        # Bidirectional BFS
        front = {0}
        back = {n - 1}
        visited = {0, n - 1}
        steps = 0

        while front:
            # Always expand the smaller set
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for idx in front:
                # Same value jumps
                for j in value_indices[arr[idx]]:
                    if j in back:
                        return steps + 1
                    if j not in visited:
                        visited.add(j)
                        next_front.add(j)

                value_indices[arr[idx]].clear()

                # Neighbor jumps
                for j in [idx - 1, idx + 1]:
                    if 0 <= j < n:
                        if j in back:
                            return steps + 1
                        if j not in visited:
                            visited.add(j)
                            next_front.add(j)

            front = next_front
            steps += 1

        return -1
