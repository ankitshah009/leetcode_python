#1215. Stepping Numbers
#Medium
#
#A stepping number is an integer such that all of its adjacent digits have an
#absolute difference of exactly 1.
#
#For example, 321 is a stepping number while 421 is not.
#
#Given two integers low and high, return a sorted list of all the stepping
#numbers in the inclusive range [low, high].
#
#Example 1:
#Input: low = 0, high = 21
#Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
#
#Example 2:
#Input: low = 10, high = 15
#Output: [10,12]
#
#Constraints:
#    0 <= low <= high <= 2 * 10^9

from typing import List
from collections import deque

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        """
        BFS: Generate stepping numbers starting from 1-9.
        Each number can generate new stepping numbers by appending
        digits that differ by 1 from the last digit.
        """
        result = []

        # Handle 0 separately
        if low <= 0 <= high:
            result.append(0)

        # BFS from each starting digit 1-9
        queue = deque(range(1, 10))

        while queue:
            num = queue.popleft()

            if num > high:
                continue

            if low <= num <= high:
                result.append(num)

            # Get last digit
            last_digit = num % 10

            # Generate next stepping numbers
            if last_digit > 0:
                next_num = num * 10 + (last_digit - 1)
                if next_num <= high:
                    queue.append(next_num)

            if last_digit < 9:
                next_num = num * 10 + (last_digit + 1)
                if next_num <= high:
                    queue.append(next_num)

        return sorted(result)


class SolutionDFS:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        """DFS approach"""
        result = []

        def dfs(num):
            if num > high:
                return

            if low <= num <= high:
                result.append(num)

            last_digit = num % 10

            if last_digit > 0:
                dfs(num * 10 + last_digit - 1)
            if last_digit < 9:
                dfs(num * 10 + last_digit + 1)

        # Start DFS from each digit 1-9
        for start in range(1, 10):
            dfs(start)

        # Handle 0
        if low <= 0:
            result.append(0)

        return sorted(result)


class SolutionIterative:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        """Iterative generation"""
        result = []

        if low == 0:
            result.append(0)

        # Generate stepping numbers level by level
        current = list(range(1, 10))

        while current:
            next_level = []

            for num in current:
                if num > high:
                    continue

                if low <= num <= high:
                    result.append(num)

                last = num % 10

                if last > 0:
                    new_num = num * 10 + last - 1
                    if new_num <= high:
                        next_level.append(new_num)

                if last < 9:
                    new_num = num * 10 + last + 1
                    if new_num <= high:
                        next_level.append(new_num)

            current = next_level

        return sorted(result)
