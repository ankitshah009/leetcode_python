#3. Longest Substring Without Repeating Characters
#Medium
#
#Given a string s, find the length of the longest substring without repeating
#characters.
#
#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#
#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#
#Example 3:
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence not substring.
#
#Constraints:
#    0 <= s.length <= 5 * 10^4
#    s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with hash set.
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


class SolutionHashMap:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimized sliding window with hash map storing last index.
        """
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


class SolutionArray:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Using array for ASCII characters (faster than hash map).
        """
        char_index = [-1] * 128
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char_index[ord(char)] >= left:
                left = char_index[ord(char)] + 1

            char_index[ord(char)] = right
            max_length = max(max_length, right - left + 1)

        return max_length


class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute force - check all substrings.
        O(n^3) time complexity.
        """
        def all_unique(substring):
            return len(substring) == len(set(substring))

        n = len(s)
        max_length = 0

        for i in range(n):
            for j in range(i, n):
                if all_unique(s[i:j+1]):
                    max_length = max(max_length, j - i + 1)

        return max_length
