#1234. Replace the Substring for Balanced String
#Medium
#
#You are given a string s of length n containing only four kinds of characters:
#'Q', 'W', 'E', and 'R'.
#
#A string is said to be balanced if each of its characters appears n / 4 times
#where n is the length of the string.
#
#Return the minimum length of the substring that can be replaced with any other
#string of the same length to make s balanced. If s is already balanced, return 0.
#
#Example 1:
#Input: s = "QWER"
#Output: 0
#Explanation: s is already balanced.
#
#Example 2:
#Input: s = "QQWE"
#Output: 1
#Explanation: We need to replace a 'Q' to 'R', so the resulting string is "RQWE"
#(or "QRWE").
#
#Example 3:
#Input: s = "QQQW"
#Output: 2
#Explanation: We can replace the first "QQ" to "ER".
#
#Constraints:
#    n == s.length
#    4 <= n <= 10^5
#    n is a multiple of 4.
#    s contains only 'Q', 'W', 'E', and 'R'.

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        """
        Sliding window: Find shortest substring such that the characters
        OUTSIDE the window are all <= n/4.

        If we replace the window, we can make all counts exactly n/4.
        """
        n = len(s)
        target = n // 4
        count = Counter(s)

        # Check if already balanced
        if all(count[c] <= target for c in 'QWER'):
            return 0

        result = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1

            # Shrink window while valid
            while left <= right and all(count[c] <= target for c in 'QWER'):
                result = min(result, right - left + 1)
                count[s[left]] += 1
                left += 1

        return result


class SolutionBinarySearch:
    def balancedString(self, s: str) -> int:
        """Binary search on answer length"""
        n = len(s)
        target = n // 4
        count = Counter(s)

        if all(count[c] <= target for c in 'QWER'):
            return 0

        def can_balance(length):
            """Can we balance by replacing a substring of given length?"""
            # Count characters in window
            window = Counter(s[:length])

            # Check if remaining chars are all <= target
            remaining = {c: count[c] - window[c] for c in 'QWER'}
            if all(remaining[c] <= target for c in 'QWER'):
                return True

            # Slide window
            for i in range(length, n):
                window[s[i]] += 1
                window[s[i - length]] -= 1
                remaining = {c: count[c] - window[c] for c in 'QWER'}
                if all(remaining[c] <= target for c in 'QWER'):
                    return True

            return False

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if can_balance(mid):
                right = mid
            else:
                left = mid + 1

        return left
