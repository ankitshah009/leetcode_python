#1999. Smallest Greater Multiple Made of Two Digits
#Medium
#
#Given three integers, k, digit1, and digit2, you want to find the smallest
#integer that is:
#- Larger than k,
#- A positive multiple of k, and
#- Comprised of only the digits digit1 and/or digit2.
#
#Return the smallest such integer. If no such integer exists or the integer
#exceeds the limit of a signed 32-bit integer (2^31 - 1), return -1.
#
#Example 1:
#Input: k = 2, digit1 = 0, digit2 = 2
#Output: 20
#
#Example 2:
#Input: k = 3, digit1 = 4, digit2 = 2
#Output: 24
#
#Example 3:
#Input: k = 2, digit1 = 0, digit2 = 0
#Output: -1
#Explanation: The only integer comprised only of 0 is 0, which is not greater
#than k.
#
#Constraints:
#    1 <= k <= 1000
#    0 <= digit1 <= 9
#    0 <= digit2 <= 9

from collections import deque

class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        """
        BFS to generate numbers using digit1 and digit2.
        """
        MAX_VAL = 2**31 - 1

        # Ensure digit1 <= digit2 for consistency
        d1, d2 = min(digit1, digit2), max(digit1, digit2)

        # Edge case: both digits are 0
        if d2 == 0:
            return -1

        # BFS: generate all valid numbers
        queue = deque()

        # Start with non-zero digits
        if d1 > 0:
            queue.append(d1)
        if d2 > 0 and d2 != d1:
            queue.append(d2)

        while queue:
            num = queue.popleft()

            if num > MAX_VAL:
                return -1

            # Check if valid
            if num > k and num % k == 0:
                return num

            # Generate next numbers
            next1 = num * 10 + d1
            next2 = num * 10 + d2

            if next1 <= MAX_VAL:
                queue.append(next1)
            if next2 <= MAX_VAL and d1 != d2:
                queue.append(next2)

        return -1


class SolutionDFS:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        """
        DFS with pruning.
        """
        MAX_VAL = 2**31 - 1
        result = [MAX_VAL + 1]

        d1, d2 = min(digit1, digit2), max(digit1, digit2)

        if d2 == 0:
            return -1

        def dfs(num: int):
            if num > MAX_VAL:
                return

            if num > k and num % k == 0:
                result[0] = min(result[0], num)
                return  # Found valid, no need to go deeper

            if num > result[0]:
                return  # Pruning

            if d1 > 0 or num > 0:  # Avoid leading zeros
                dfs(num * 10 + d1)
            if d2 != d1:
                dfs(num * 10 + d2)

        # Start DFS
        if d1 > 0:
            dfs(d1)
        if d2 > 0 and d2 != d1:
            dfs(d2)

        return result[0] if result[0] <= MAX_VAL else -1


class SolutionBruteForce:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        """
        Brute force: check multiples of k.
        """
        MAX_VAL = 2**31 - 1
        valid_digits = {str(digit1), str(digit2)}

        multiple = k * 2  # Start from smallest multiple > k

        while multiple <= MAX_VAL:
            if all(c in valid_digits for c in str(multiple)):
                return multiple
            multiple += k

        return -1
