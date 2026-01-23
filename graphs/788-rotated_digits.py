#788. Rotated Digits
#Medium
#
#An integer x is a good number if after rotating each digit individually by
#180 degrees, we get a valid number that is different from x. Each digit must
#be rotated - we cannot choose to leave it alone.
#
#A number is valid if each digit remains a digit after rotation. For example:
#- 0, 1, and 8 rotate to themselves,
#- 2 and 5 rotate to each other (2 becomes 5 and 5 becomes 2),
#- 6 and 9 rotate to each other (6 becomes 9 and 9 becomes 6), and
#- the rest of the numbers do not rotate to any other number and become invalid.
#
#Given an integer n, return the number of good integers in the range [1, n].
#
#Example 1:
#Input: n = 10
#Output: 4
#Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
#
#Example 2:
#Input: n = 1
#Output: 0
#
#Example 3:
#Input: n = 2
#Output: 1
#
#Constraints:
#    1 <= n <= 10^4

class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        A number is good if:
        - Contains only 0,1,2,5,6,8,9 (valid after rotation)
        - Contains at least one of 2,5,6,9 (different after rotation)
        """
        count = 0

        for num in range(1, n + 1):
            s = str(num)
            if any(d in s for d in '347'):
                continue
            if any(d in s for d in '2569'):
                count += 1

        return count


class SolutionDigitDP:
    """Digit DP for larger n"""

    def rotatedDigits(self, n: int) -> int:
        from functools import lru_cache

        s = str(n)

        @lru_cache(maxsize=None)
        def dp(pos, tight, has_diff):
            if pos == len(s):
                return 1 if has_diff else 0

            limit = int(s[pos]) if tight else 9
            count = 0

            for d in range(limit + 1):
                if d in (3, 4, 7):
                    continue
                new_tight = tight and (d == limit)
                new_diff = has_diff or (d in (2, 5, 6, 9))
                count += dp(pos + 1, new_tight, new_diff)

            return count

        return dp(0, True, False)


class SolutionSet:
    """Using set operations"""

    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        different = {'2', '5', '6', '9'}

        count = 0
        for num in range(1, n + 1):
            digits = set(str(num))
            if digits <= valid and digits & different:
                count += 1

        return count
