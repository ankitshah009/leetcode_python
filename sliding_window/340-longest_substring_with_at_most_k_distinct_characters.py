#340. Longest Substring with At Most K Distinct Characters
#Medium
#
#Given a string s and an integer k, return the length of the longest substring of s that
#contains at most k distinct characters.
#
#Example 1:
#Input: s = "eceba", k = 2
#Output: 3
#Explanation: The substring is "ece" with length 3.
#
#Example 2:
#Input: s = "aa", k = 1
#Output: 2
#Explanation: The substring is "aa" with length 2.
#
#Constraints:
#    1 <= s.length <= 5 * 10^4
#    0 <= k <= 50

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
