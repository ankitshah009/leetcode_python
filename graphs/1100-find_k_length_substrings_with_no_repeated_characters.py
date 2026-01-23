#1100. Find K-Length Substrings With No Repeated Characters
#Medium
#
#Given a string s and an integer k, return the number of substrings in s
#of length k with no repeated characters.
#
#Example 1:
#Input: s = "havefunonleetcode", k = 5
#Output: 6
#Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno',
#'etcod','tcode'.
#
#Example 2:
#Input: s = "home", k = 5
#Output: 0
#Explanation: Notice k can be larger than the length of s. In this case,
#it is not possible to find any substring.
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of lowercase English letters.
#    1 <= k <= 10^4

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        Sliding window with character count.
        """
        if k > len(s):
            return 0

        count = {}
        result = 0

        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1

            # Remove leftmost character when window exceeds k
            if i >= k:
                left_char = s[i - k]
                count[left_char] -= 1
                if count[left_char] == 0:
                    del count[left_char]

            # Check if window has k unique characters
            if i >= k - 1 and len(count) == k:
                result += 1

        return result


class SolutionSet:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """Using set and checking window"""
        if k > len(s):
            return 0

        result = 0

        for i in range(len(s) - k + 1):
            window = s[i:i + k]
            if len(set(window)) == k:
                result += 1

        return result


class SolutionOptimized:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """Track duplicate count"""
        if k > len(s) or k > 26:
            return 0

        count = [0] * 26
        duplicates = 0
        result = 0

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if count[idx] == 1:
                duplicates += 1
            count[idx] += 1

            if i >= k:
                left_idx = ord(s[i - k]) - ord('a')
                count[left_idx] -= 1
                if count[left_idx] == 1:
                    duplicates -= 1

            if i >= k - 1 and duplicates == 0:
                result += 1

        return result
