#1016. Binary String With Substrings Representing 1 To N
#Medium
#
#Given a binary string s and a positive integer n, return true if the binary
#representation of all the integers in the range [1, n] are substrings of s,
#or false otherwise.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "0110", n = 3
#Output: true
#
#Example 2:
#Input: s = "0110", n = 4
#Output: false
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either '0' or '1'.
#    1 <= n <= 10^9

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """
        Check if binary representation of each number is in s.
        Optimization: only need to check n down to n/2 + 1.
        """
        # If n is too large for s to contain all representations
        if n > len(s) * 2:
            return False

        for i in range(n, 0, -1):
            if bin(i)[2:] not in s:
                return False

        return True


class SolutionSet:
    """Extract all numbers from s"""

    def queryString(self, s: str, n: int) -> bool:
        if n > len(s) * 2:
            return False

        # Extract all binary substrings as numbers
        found = set()
        m = len(s)

        # For each starting position
        for i in range(m):
            if s[i] == '0':
                continue  # Skip leading zeros (except for 0 itself)

            num = 0
            for j in range(i, min(i + 30, m)):  # 30 bits is enough
                num = num * 2 + int(s[j])
                if num > n:
                    break
                found.add(num)

        return all(i in found for i in range(1, n + 1))


class SolutionOptimized:
    """Optimized check - only check larger half"""

    def queryString(self, s: str, n: int) -> bool:
        """
        Key insight: if all numbers from n/2+1 to n are substrings,
        their right-shifted versions (1 to n/2) are also substrings.
        """
        # Check numbers from n down to n/2 + 1
        for i in range(n, n // 2, -1):
            if bin(i)[2:] not in s:
                return False

        return True
