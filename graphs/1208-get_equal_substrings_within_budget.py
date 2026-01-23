#1208. Get Equal Substrings Within Budget
#Medium
#
#You are given two strings s and t of the same length and an integer maxCost.
#
#You want to change s to t. Changing the ith character of s to ith character
#of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII
#values of the characters).
#
#Return the maximum length of a substring of s that can be changed to be the
#same as the corresponding substring of t with a cost less than or equal to maxCost.
#If there is no substring from s that can be changed to its corresponding
#substring from t, return 0.
#
#Example 1:
#Input: s = "abcd", t = "bcdf", maxCost = 3
#Output: 3
#Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
#
#Example 2:
#Input: s = "abcd", t = "cdef", maxCost = 3
#Output: 1
#Explanation: Each character in s costs 2 to change to character in t, so the
#maximum length is 1.
#
#Example 3:
#Input: s = "abcd", t = "acde", maxCost = 0
#Output: 1
#Explanation: You cannot make any change, so the maximum length is 1.
#
#Constraints:
#    1 <= s.length <= 10^5
#    t.length == s.length
#    0 <= maxCost <= 10^6
#    s and t consist of only lowercase English letters.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Sliding window: Find longest window where sum of costs <= maxCost.
        """
        n = len(s)
        left = 0
        current_cost = 0
        max_length = 0

        for right in range(n):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            # Shrink window if cost exceeds budget
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


class SolutionPrefixSum:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """Using prefix sum and binary search"""
        import bisect

        n = len(s)

        # Build cost array and prefix sum
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + costs[i]

        max_length = 0

        for right in range(n):
            # Find leftmost position where prefix[right+1] - prefix[left] <= maxCost
            # prefix[left] >= prefix[right+1] - maxCost
            target = prefix[right + 1] - maxCost
            left = bisect.bisect_left(prefix, target, 0, right + 2)

            max_length = max(max_length, right - left + 1)

        return max_length


class SolutionOptimized:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """Optimized sliding window - never shrink window"""
        n = len(s)
        left = 0
        current_cost = 0

        for right in range(n):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            if current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

        return n - left
