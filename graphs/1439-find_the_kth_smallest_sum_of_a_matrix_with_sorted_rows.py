#1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
#Hard
#
#You are given an m x n matrix mat that has its rows sorted in non-decreasing
#order and an integer k.
#
#You are allowed to choose exactly one element from each row to form an array.
#Return the kth smallest array sum among all possible arrays.
#
#Example 1:
#Input: mat = [[1,3,11],[2,4,6]], k = 5
#Output: 7
#Explanation: Choosing one element from each row, the first k smallest sum are:
#[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
#
#Example 2:
#Input: mat = [[1,3,11],[2,4,6]], k = 9
#Output: 17
#
#Example 3:
#Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
#Output: 9
#Explanation: Choosing one element from each row, the first k smallest sum are:
#[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 40
#    1 <= mat[i][j] <= 5000
#    1 <= k <= min(200, n^m)
#    mat[i] is a non-decreasing array.

from typing import List
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        Merge rows pairwise, keeping only k smallest sums.
        Like merging k sorted lists repeatedly.
        """
        def merge_two_rows(row1: List[int], row2: List[int], k: int) -> List[int]:
            """Merge two sorted rows, return k smallest sums"""
            # Min heap: (sum, idx1, idx2)
            heap = [(row1[0] + row2[0], 0, 0)]
            visited = {(0, 0)}
            result = []

            while heap and len(result) < k:
                total, i, j = heapq.heappop(heap)
                result.append(total)

                # Try (i+1, j)
                if i + 1 < len(row1) and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    heapq.heappush(heap, (row1[i + 1] + row2[j], i + 1, j))

                # Try (i, j+1)
                if j + 1 < len(row2) and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    heapq.heappush(heap, (row1[i] + row2[j + 1], i, j + 1))

            return result

        # Start with first row
        current = mat[0][:k]

        # Merge with each subsequent row
        for row in mat[1:]:
            current = merge_two_rows(current, row[:k], k)

        return current[k - 1]


class SolutionBinarySearch:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """Binary search on answer"""
        m, n = len(mat), len(mat[0])

        def count_le(target: int) -> int:
            """Count arrays with sum <= target"""
            # Use DFS with memoization
            count = [0]

            def dfs(row: int, current_sum: int):
                if count[0] > k:
                    return
                if row == m:
                    count[0] += 1
                    return

                for j in range(n):
                    if current_sum + mat[row][j] <= target:
                        dfs(row + 1, current_sum + mat[row][j])
                    else:
                        break

            dfs(0, 0)
            return count[0]

        # Binary search
        lo = sum(row[0] for row in mat)
        hi = sum(row[-1] for row in mat)

        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo


class SolutionPQ:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """Priority queue with state tracking"""
        m, n = len(mat), len(mat[0])

        # Initial state: all zeros
        initial_sum = sum(row[0] for row in mat)
        initial_indices = tuple([0] * m)

        heap = [(initial_sum, initial_indices)]
        visited = {initial_indices}

        for _ in range(k):
            current_sum, indices = heapq.heappop(heap)

            if _ == k - 1:
                return current_sum

            # Try incrementing each row's index
            for row in range(m):
                if indices[row] + 1 < n:
                    new_indices = list(indices)
                    new_indices[row] += 1
                    new_indices = tuple(new_indices)

                    if new_indices not in visited:
                        visited.add(new_indices)
                        new_sum = current_sum - mat[row][indices[row]] + mat[row][indices[row] + 1]
                        heapq.heappush(heap, (new_sum, new_indices))

        return -1  # Should not reach here
