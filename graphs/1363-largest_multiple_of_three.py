#1363. Largest Multiple of Three
#Hard
#
#Given an array of digits digits, return the largest multiple of three that can
#be formed by concatenating some of the given digits in any order. If there is
#no answer return an empty string.
#
#Since the answer may not fit in an integer data type, return the answer as a string.
#
#Example 1:
#Input: digits = [8,1,9]
#Output: "981"
#
#Example 2:
#Input: digits = [8,6,7,1,0]
#Output: "8760"
#
#Example 3:
#Input: digits = [1]
#Output: ""
#
#Constraints:
#    1 <= digits.length <= 10^4
#    0 <= digits[i] <= 9

from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        """
        A number is divisible by 3 if sum of digits is divisible by 3.

        Strategy:
        1. Calculate total sum
        2. If sum % 3 == 0: use all digits
        3. If sum % 3 == 1: remove smallest digit with remainder 1, or two smallest with remainder 2
        4. If sum % 3 == 2: remove smallest digit with remainder 2, or two smallest with remainder 1
        """
        # Sort digits descending for largest number
        digits.sort(reverse=True)

        total = sum(digits)

        if total % 3 == 0:
            return self.format_result(digits)

        # Group by remainder
        rem_1 = sorted([d for d in digits if d % 3 == 1])
        rem_2 = sorted([d for d in digits if d % 3 == 2])

        if total % 3 == 1:
            # Remove one digit with remainder 1, or two with remainder 2
            if rem_1:
                digits.remove(rem_1[0])
            elif len(rem_2) >= 2:
                digits.remove(rem_2[0])
                digits.remove(rem_2[1])
            else:
                return ""
        else:  # total % 3 == 2
            # Remove one digit with remainder 2, or two with remainder 1
            if rem_2:
                digits.remove(rem_2[0])
            elif len(rem_1) >= 2:
                digits.remove(rem_1[0])
                digits.remove(rem_1[1])
            else:
                return ""

        return self.format_result(digits)

    def format_result(self, digits):
        if not digits:
            return ""
        if digits[0] == 0:
            return "0"
        return ''.join(map(str, digits))


class SolutionDP:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        """DP approach tracking best result for each remainder"""
        digits.sort(reverse=True)

        # best[i] = list of digits forming largest number with sum % 3 == i
        best = [[], None, None]

        for d in digits:
            # Create new candidates
            new_best = [b[:] if b is not None else None for b in best]

            for r in range(3):
                if best[r] is not None:
                    new_r = (r + d) % 3
                    candidate = best[r] + [d]

                    if new_best[new_r] is None or self.is_larger(candidate, new_best[new_r]):
                        new_best[new_r] = candidate

            # Also consider starting fresh with just d
            if new_best[d % 3] is None or self.is_larger([d], new_best[d % 3]):
                new_best[d % 3] = [d]

            best = new_best

        if best[0] is None or not best[0]:
            return ""
        if best[0][0] == 0:
            return "0"
        return ''.join(map(str, best[0]))

    def is_larger(self, a, b):
        if len(a) != len(b):
            return len(a) > len(b)
        return a > b
