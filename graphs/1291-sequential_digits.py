#1291. Sequential Digits
#Medium
#
#An integer has sequential digits if and only if each digit in the number is
#one more than the previous digit.
#
#Return a sorted list of all the integers in the range [low, high] inclusive
#that have sequential digits.
#
#Example 1:
#Input: low = 100, high = 300
#Output: [123,234]
#
#Example 2:
#Input: low = 1000, high = 13000
#Output: [1234,2345,3456,4567,5678,6789,12345]
#
#Constraints:
#    10 <= low <= high <= 10^9

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Generate all sequential digit numbers from "123456789".
        """
        sample = "123456789"
        result = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result


class SolutionBFS:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """Generate using BFS"""
        from collections import deque

        result = []
        queue = deque(range(1, 10))

        while queue:
            num = queue.popleft()
            if low <= num <= high:
                result.append(num)

            last_digit = num % 10
            if last_digit < 9:
                next_num = num * 10 + last_digit + 1
                if next_num <= high:
                    queue.append(next_num)

        return sorted(result)


class SolutionPrecompute:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """Precompute all possible sequential digit numbers"""
        all_sequential = []
        for length in range(2, 10):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                all_sequential.append(num)

        return [x for x in all_sequential if low <= x <= high]
