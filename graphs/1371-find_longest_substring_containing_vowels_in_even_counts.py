#1371. Find the Longest Substring Containing Vowels in Even Counts
#Medium
#
#Given the string s, return the size of the longest substring containing each
#vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear
#an even number of times.
#
#Example 1:
#Input: s = "eleetminicoworoep"
#Output: 13
#Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
#
#Example 2:
#Input: s = "leetcodeisgreat"
#Output: 5
#Explanation: The longest substring is "leetc" which contains two e's.
#
#Example 3:
#Input: s = "bcbcbc"
#Output: 6
#Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
#
#Constraints:
#    1 <= s.length <= 5 x 10^5
#    s contains only lowercase English letters.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        Use bitmask to track parity of each vowel.
        Same bitmask at two positions means all vowels have even count between them.
        """
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        # First occurrence of each state
        # State 0 (all even) first occurs at index -1 (before string starts)
        first_occurrence = {0: -1}

        state = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in vowels:
                state ^= (1 << vowels[c])

            if state in first_occurrence:
                max_len = max(max_len, i - first_occurrence[state])
            else:
                first_occurrence[state] = i

        return max_len


class SolutionArray:
    def findTheLongestSubstring(self, s: str) -> int:
        """Using array for first occurrence (faster lookup)"""
        # 32 possible states (5 vowels, 2^5 = 32)
        first = [-2] * 32  # -2 means not seen
        first[0] = -1  # State 0 starts at -1

        vowel_bit = [0] * 26
        vowel_bit[ord('a') - ord('a')] = 1
        vowel_bit[ord('e') - ord('a')] = 2
        vowel_bit[ord('i') - ord('a')] = 4
        vowel_bit[ord('o') - ord('a')] = 8
        vowel_bit[ord('u') - ord('a')] = 16

        state = 0
        max_len = 0

        for i, c in enumerate(s):
            state ^= vowel_bit[ord(c) - ord('a')]

            if first[state] != -2:
                max_len = max(max_len, i - first[state])
            else:
                first[state] = i

        return max_len
