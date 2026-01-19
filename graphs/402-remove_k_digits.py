#402. Remove K Digits
#Medium
#
#Given string num representing a non-negative integer num, and an integer k,
#return the smallest possible integer after removing k digits from num.
#
#Example 1:
#Input: num = "1432219", k = 3
#Output: "1219"
#Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
#which is the smallest.
#
#Example 2:
#Input: num = "10200", k = 1
#Output: "200"
#Explanation: Remove the leading 1 and the number is 200. Note that the output
#must not contain leading zeroes.
#
#Example 3:
#Input: num = "10", k = 2
#Output: "0"
#Explanation: Remove all the digits from the number and it is left with nothing
#which is 0.
#
#Constraints:
#    1 <= k <= num.length <= 10^5
#    num consists of only digits.
#    num does not have any leading zeros except for the zero itself.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Monotonic stack approach.
        Greedily remove larger digits when possible.
        """
        stack = []

        for digit in num:
            # Remove larger digits from stack while we can
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k > 0, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros and return
        result = ''.join(stack).lstrip('0')
        return result if result else '0'


class SolutionDetailed:
    """More explicit handling of edge cases"""

    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove remaining k digits from the end
        stack = stack[:-k] if k else stack

        # Build result, removing leading zeros
        result = ''.join(stack).lstrip('0')

        return result or "0"


class SolutionGreedy:
    """Alternative greedy approach"""

    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n:
            return "0"

        # Result will have n - k digits
        result_len = n - k
        result = []

        for i, digit in enumerate(num):
            # While we can still remove and current digit is smaller
            while result and len(result) + (n - i) > result_len and result[-1] > digit:
                result.pop()
            if len(result) < result_len:
                result.append(digit)

        return ''.join(result).lstrip('0') or "0"
