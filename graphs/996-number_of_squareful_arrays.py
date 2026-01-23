#996. Number of Squareful Arrays
#Hard
#
#An array is squareful if the sum of every pair of adjacent elements is a
#perfect square.
#
#Given an integer array nums, return the number of permutations of nums that
#are squareful.
#
#Two permutations perm1 and perm2 are different if there is some index i such
#that perm1[i] != perm2[i].
#
#Example 1:
#Input: nums = [1,17,8]
#Output: 2
#Explanation: [1,8,17] and [17,8,1] are the valid permutations.
#
#Example 2:
#Input: nums = [2,2,2]
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 12
#    0 <= nums[i] <= 10^9

from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        """
        Backtracking with deduplication.
        """
        def is_square(n):
            root = int(n ** 0.5)
            return root * root == n

        count = Counter(nums)
        n = len(nums)

        # Build graph: which numbers can be adjacent
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if is_square(x + y):
                    graph[x].append(y)

        result = 0

        def backtrack(last, length):
            nonlocal result

            if length == n:
                result += 1
                return

            for neighbor in graph[last]:
                if count[neighbor] > 0:
                    count[neighbor] -= 1
                    backtrack(neighbor, length + 1)
                    count[neighbor] += 1

        # Try each unique number as starting point
        for num in count:
            count[num] -= 1
            backtrack(num, 1)
            count[num] += 1

        return result


class SolutionBitmask:
    """Bitmask DP"""

    def numSquarefulPerms(self, nums: list[int]) -> int:
        from functools import lru_cache

        def is_square(n):
            root = int(n ** 0.5)
            return root * root == n

        n = len(nums)
        nums.sort()

        @lru_cache(maxsize=None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1

            result = 0
            prev = None

            for i in range(n):
                if mask & (1 << i):
                    continue
                if nums[i] == prev:
                    continue
                if last != -1 and not is_square(nums[last] + nums[i]):
                    continue

                prev = nums[i]
                result += dp(mask | (1 << i), i)

            return result

        return dp(0, -1)


class SolutionDFS:
    """DFS with pruning"""

    def numSquarefulPerms(self, nums: list[int]) -> int:
        def is_square(n):
            root = int(n ** 0.5)
            return root * root == n

        nums.sort()
        n = len(nums)
        result = [0]
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                result[0] += 1
                return

            for i in range(n):
                if used[i]:
                    continue
                # Skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                # Check squareful condition
                if path and not is_square(path[-1] + nums[i]):
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return result[0]
