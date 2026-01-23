#526. Beautiful Arrangement
#Medium
#
#Suppose you have n integers labeled 1 through n. A permutation of those n integers
#perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n),
#either of the following is true:
#- perm[i] is divisible by i.
#- i is divisible by perm[i].
#
#Given an integer n, return the number of the beautiful arrangements that you can construct.
#
#Example 1:
#Input: n = 2
#Output: 2
#Explanation:
#The first beautiful arrangement is [1,2]:
#    - perm[1] = 1 is divisible by i = 1
#    - perm[2] = 2 is divisible by i = 2
#The second beautiful arrangement is [2,1]:
#    - perm[1] = 2 is divisible by i = 1
#    - i = 2 is divisible by perm[2] = 1
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 15

class Solution:
    def countArrangement(self, n: int) -> int:
        """Backtracking with pruning"""
        count = 0
        used = [False] * (n + 1)

        def backtrack(pos):
            nonlocal count
            if pos > n:
                count += 1
                return

            for num in range(1, n + 1):
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True
                    backtrack(pos + 1)
                    used[num] = False

        backtrack(1)
        return count


class SolutionBitmask:
    """Bitmask DP"""

    def countArrangement(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(pos, mask):
            if pos > n:
                return 1

            count = 0
            for num in range(1, n + 1):
                if not (mask & (1 << num)) and (num % pos == 0 or pos % num == 0):
                    count += dp(pos + 1, mask | (1 << num))

            return count

        return dp(1, 0)


class SolutionSwap:
    """Backtracking using swaps"""

    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        count = 0

        def backtrack(pos):
            nonlocal count
            if pos == 0:
                count += 1
                return

            for i in range(pos):
                nums[i], nums[pos - 1] = nums[pos - 1], nums[i]
                if nums[pos - 1] % pos == 0 or pos % nums[pos - 1] == 0:
                    backtrack(pos - 1)
                nums[i], nums[pos - 1] = nums[pos - 1], nums[i]

        backtrack(n)
        return count
