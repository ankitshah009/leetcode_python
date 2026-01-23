#967. Numbers With Same Consecutive Differences
#Medium
#
#Given two integers n and k, return an array of all the integers of length n
#where the difference between every two consecutive digits is k. You may return
#the answer in any order.
#
#Note that the integers should not have leading zeros except for 0 itself.
#
#Example 1:
#Input: n = 3, k = 7
#Output: [181,292,707,818,929]
#
#Example 2:
#Input: n = 2, k = 1
#Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#Constraints:
#    2 <= n <= 9
#    0 <= k <= 9

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """
        BFS building numbers digit by digit.
        """
        # Start with single digits 1-9 (no leading zero)
        current = list(range(1, 10))

        for _ in range(n - 1):
            next_nums = []
            for num in current:
                last_digit = num % 10

                # Add digit that differs by k
                if last_digit + k <= 9:
                    next_nums.append(num * 10 + last_digit + k)
                if k != 0 and last_digit - k >= 0:
                    next_nums.append(num * 10 + last_digit - k)

            current = next_nums

        return current if n > 1 else list(range(10))


class SolutionDFS:
    """DFS backtracking"""

    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        result = []

        def dfs(num: int, length: int):
            if length == n:
                result.append(num)
                return

            last_digit = num % 10

            next_digits = set()
            if last_digit + k <= 9:
                next_digits.add(last_digit + k)
            if last_digit - k >= 0:
                next_digits.add(last_digit - k)

            for d in next_digits:
                dfs(num * 10 + d, length + 1)

        for start in range(1, 10):
            dfs(start, 1)

        return result


class SolutionIterative:
    """Iterative set-based"""

    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        if n == 1:
            return list(range(10))

        nums = set(range(1, 10))

        for _ in range(n - 1):
            new_nums = set()
            for num in nums:
                last = num % 10
                if last + k <= 9:
                    new_nums.add(num * 10 + last + k)
                if last - k >= 0:
                    new_nums.add(num * 10 + last - k)
            nums = new_nums

        return list(nums)
