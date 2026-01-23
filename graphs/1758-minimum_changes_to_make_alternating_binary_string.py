#1758. Minimum Changes To Make Alternating Binary String
#Easy
#
#You are given a string s consisting only of the characters '0' and '1'. In one
#operation, you can change any '0' to '1' or vice versa.
#
#The string is called alternating if no two adjacent characters are equal. For
#example, the string "010" is alternating, while the string "0100" is not.
#
#Return the minimum number of operations needed to make s alternating.
#
#Example 1:
#Input: s = "0100"
#Output: 1
#
#Example 2:
#Input: s = "10"
#Output: 0
#
#Example 3:
#Input: s = "1111"
#Output: 2
#
#Constraints:
#    1 <= s.length <= 10^4
#    s[i] is either '0' or '1'.

class Solution:
    def minOperations(self, s: str) -> int:
        """
        Compare with two patterns: "010101..." and "101010..."
        Return minimum changes needed.
        """
        # Count mismatches with pattern starting with '0'
        changes_start_0 = sum(1 for i, c in enumerate(s) if c != str(i % 2))

        # Changes for pattern starting with '1' = n - changes_start_0
        changes_start_1 = len(s) - changes_start_0

        return min(changes_start_0, changes_start_1)


class SolutionExplicit:
    def minOperations(self, s: str) -> int:
        """
        Explicitly count both patterns.
        """
        count1 = 0  # Pattern "010101..."
        count2 = 0  # Pattern "101010..."

        for i, c in enumerate(s):
            expected1 = '0' if i % 2 == 0 else '1'
            expected2 = '1' if i % 2 == 0 else '0'

            if c != expected1:
                count1 += 1
            if c != expected2:
                count2 += 1

        return min(count1, count2)


class SolutionOnePass:
    def minOperations(self, s: str) -> int:
        """
        Single pass counting.
        """
        n = len(s)
        mismatch_even_0 = 0  # Positions where even index should be '0' but isn't

        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == '1':
                    mismatch_even_0 += 1
            else:
                if c == '0':
                    mismatch_even_0 += 1

        return min(mismatch_even_0, n - mismatch_even_0)
