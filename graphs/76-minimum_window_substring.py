#76. Minimum Window Substring
#Hard
#
#Given two strings s and t of lengths m and n respectively, return the minimum
#window substring of s such that every character in t (including duplicates) is
#included in the window. If there is no such substring, return the empty string "".
#
#The testcases will be generated such that the answer is unique.
#
#Example 1:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from
#string t.
#
#Example 2:
#Input: s = "a", t = "a"
#Output: "a"
#
#Example 3:
#Input: s = "a", t = "aa"
#Output: ""
#Explanation: Both 'a's from t must be included in the window.
#
#Constraints:
#    m == s.length
#    n == t.length
#    1 <= m, n <= 10^5
#    s and t consist of uppercase and lowercase English letters.
#
#Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window with character counting.
        """
        if not s or not t or len(s) < len(t):
            return ""

        t_count = Counter(t)
        required = len(t_count)
        formed = 0

        window_count = {}
        left = 0
        min_len = float('inf')
        result = (0, 0)

        for right, char in enumerate(s):
            # Expand window
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Contract window
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)

                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[result[0]:result[1] + 1]


class SolutionOptimized:
    def minWindow(self, s: str, t: str) -> str:
        """
        Optimized with filtered s (only characters in t).
        """
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)

        # Filter s to only include characters in t
        filtered_s = [(i, char) for i, char in enumerate(s) if char in t_count]

        left = 0
        formed = 0
        window_count = {}
        result = (float('inf'), None, None)

        for right, (right_idx, char) in enumerate(filtered_s):
            window_count[char] = window_count.get(char, 0) + 1

            if window_count[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                left_idx, left_char = filtered_s[left]

                if right_idx - left_idx + 1 < result[0]:
                    result = (right_idx - left_idx + 1, left_idx, right_idx)

                window_count[left_char] -= 1
                if window_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1

        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


class SolutionSimple:
    def minWindow(self, s: str, t: str) -> str:
        """
        Simpler implementation with have/need tracking.
        """
        if len(t) > len(s):
            return ""

        need = Counter(t)
        have = {}
        need_count = len(need)
        have_count = 0

        result = ""
        min_len = float('inf')
        left = 0

        for right, char in enumerate(s):
            if char in need:
                have[char] = have.get(char, 0) + 1
                if have[char] == need[char]:
                    have_count += 1

            while have_count == need_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                if s[left] in need:
                    have[s[left]] -= 1
                    if have[s[left]] < need[s[left]]:
                        have_count -= 1

                left += 1

        return result
