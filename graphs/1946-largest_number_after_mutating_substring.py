#1946. Largest Number After Mutating Substring
#Medium
#
#You are given a string num, which represents a large integer. You are also
#given a 0-indexed integer array change of length 10 that maps each digit 0-9
#to another digit. More formally, digit d maps to digit change[d].
#
#You may choose to mutate a single substring of num. To mutate a substring,
#replace each digit num[i] with the digit it maps to in change (i.e. replace
#num[i] with change[num[i]]).
#
#Return a string representing the largest possible integer after mutating (or
#choosing not to) a single substring of num.
#
#A substring is a contiguous sequence of characters within the string.
#
#Example 1:
#Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
#Output: "832"
#
#Example 2:
#Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
#Output: "934"
#
#Example 3:
#Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
#Output: "5"
#
#Constraints:
#    1 <= num.length <= 10^5
#    num consists of only digits 0-9.
#    change.length == 10
#    0 <= change[i] <= 9

from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        """
        Greedy: start mutation when beneficial, stop when not.
        """
        result = list(num)
        started = False

        for i, c in enumerate(num):
            d = int(c)
            mapped = change[d]

            if mapped > d:
                result[i] = str(mapped)
                started = True
            elif mapped < d:
                if started:
                    break
            # If equal, continue (keep original or continue mutation)

        return ''.join(result)


class SolutionExplained:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        """
        Detailed explanation:

        Find leftmost position where change improves digit.
        Continue mutating while change >= original digit.
        Stop when change < original digit.
        """
        digits = list(num)
        n = len(digits)
        i = 0

        # Skip leading digits where change doesn't improve
        while i < n and change[int(digits[i])] <= int(digits[i]):
            i += 1

        # Mutate while change >= original
        while i < n and change[int(digits[i])] >= int(digits[i]):
            digits[i] = str(change[int(digits[i])])
            i += 1

        return ''.join(digits)
