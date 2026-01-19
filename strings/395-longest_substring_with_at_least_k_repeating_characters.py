#395. Longest Substring with At Least K Repeating Characters
#Medium
#
#Given a string s and an integer k, return the length of the longest substring of s such that
#the frequency of each character in this substring is greater than or equal to k.
#
#if no such substring exists, return 0.
#
#Example 1:
#Input: s = "aaabb", k = 3
#Output: 3
#Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#
#Example 2:
#Input: s = "ababbc", k = 2
#Output: 5
#Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of only lowercase English letters.
#    1 <= k <= 10^5

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # Count frequency
        count = Counter(s)

        # Find a character that appears less than k times
        for char, freq in count.items():
            if freq < k:
                # Split by this character and recurse
                return max(self.longestSubstring(substring, k)
                          for substring in s.split(char))

        # All characters appear at least k times
        return len(s)
