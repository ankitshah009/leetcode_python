#1663. Smallest String With A Given Numeric Value
#Medium
#
#The numeric value of a lowercase character is defined as its position (1-indexed)
#in the alphabet, so the numeric value of a is 1, the numeric value of b is 2,
#and so on. The numeric value of a string is the sum of its characters' numeric values.
#
#You are given two integers n and k. Return the lexicographically smallest string
#with length equal to n and numeric value equal to k.
#
#Note that a string x is lexicographically smaller than string y if x comes
#before y in dictionary order.
#
#Example 1:
#Input: n = 3, k = 27
#Output: "aay"
#Explanation: "aay" has value 1 + 1 + 25 = 27.
#
#Example 2:
#Input: n = 5, k = 73
#Output: "aaszz"
#Explanation: "aaszz" has value 1 + 1 + 19 + 26 + 26 = 73.
#
#Constraints:
#    1 <= n <= 10^5
#    n <= k <= 26 * n

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Greedy: Fill with 'a's, then add 'z's from right.
        """
        # Start with all 'a's (value = n)
        result = ['a'] * n
        remaining = k - n  # How much more value we need

        # Fill from right with 'z' (adds 25 each time)
        i = n - 1
        while remaining > 0:
            add = min(25, remaining)
            result[i] = chr(ord('a') + add)
            remaining -= add
            i -= 1

        return ''.join(result)


class SolutionMath:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Calculate exact counts mathematically.
        """
        # We want: (n - count_z) * 1 + count_z * 26 + middle_char = k
        # Simplify: n + 25 * count_z + (middle - 1) = k

        # Number of 'z's we can fit
        excess = k - n  # Extra value beyond all 'a's
        count_z = excess // 25
        remainder = excess % 25

        count_a = n - count_z - (1 if remainder > 0 else 0)
        middle = chr(ord('a') + remainder) if remainder > 0 else ''

        return 'a' * count_a + middle + 'z' * count_z


class SolutionDirect:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Direct calculation approach.
        """
        result = []

        for i in range(n):
            # Positions left after this one
            remaining_pos = n - i - 1
            # Minimum value we need for remaining positions
            min_remaining = remaining_pos  # All 'a's

            # Current character should be as small as possible
            # But remaining must be achievable (value <= 26 * remaining_pos)
            for c in range(1, 27):
                if c + remaining_pos <= k <= c + remaining_pos * 26:
                    result.append(chr(ord('a') + c - 1))
                    k -= c
                    break

        return ''.join(result)


class SolutionSimple:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Simple greedy with clear logic.
        """
        result = []

        for i in range(n):
            remaining = n - i - 1  # Positions after current

            # What's the smallest char we can put here?
            # Need: char_value + remaining_sum = k - (sum so far)
            # remaining_sum can be at most 26 * remaining

            for val in range(1, 27):  # 'a' to 'z'
                if val + 26 * remaining >= k:
                    result.append(chr(ord('a') + val - 1))
                    k -= val
                    break

        return ''.join(result)


class SolutionOptimal:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Optimal O(1) calculation (excluding string building).
        """
        # How many 'z's fit?
        # k = a_count * 1 + z_count * 26 + middle_val
        # n = a_count + z_count + (1 if middle else 0)

        # If we use z_count z's, remaining value = k - 26*z_count
        # Remaining positions = n - z_count
        # For lexicographically smallest, maximize a's

        z_count = 0
        while k - 26 * (z_count + 1) >= n - z_count - 1:
            z_count += 1

        remaining = k - 26 * z_count
        a_count = n - z_count - 1

        if remaining <= 0:
            a_count = n - z_count
            middle = ''
        else:
            middle = chr(ord('a') + remaining - 1)

        return 'a' * a_count + middle + 'z' * z_count
