#76. Minimum Window Substring
#Hard
#
#Given two strings s and t of lengths m and n respectively, return the minimum window
#substring of s such that every character in t (including duplicates) is included in the window.
#If there is no such substring, return the empty string "".
#
#The testcases will be generated such that the answer is unique.
#
#Example 1:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#
#Example 2:
#Input: s = "a", t = "a"
#Output: "a"
#Explanation: The entire string s is the minimum window.
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

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        required = len(t_count)

        left = 0
        formed = 0
        window_counts = {}

        min_len = float('inf')
        min_left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                char = s[left]
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
