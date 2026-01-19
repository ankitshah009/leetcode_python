#438. Find All Anagrams in a String
#Medium
#
#Given two strings s and p, return an array of all the start indices of p's anagrams in s.
#You may return the answer in any order.
#
#An Anagram is a word or phrase formed by rearranging the letters of a different word or
#phrase, typically using all the original letters exactly once.
#
#Example 1:
#Input: s = "cbaebabacd", p = "abc"
#Output: [0,6]
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#Example 2:
#Input: s = "abab", p = "ab"
#Output: [0,1,2]
#
#Constraints:
#    1 <= s.length, p.length <= 3 * 10^4
#    s and p consist of lowercase English letters.

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        result = []

        if s_count == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            # Add new character
            s_count[s[i]] += 1

            # Remove old character
            old_char = s[i - len(p)]
            s_count[old_char] -= 1
            if s_count[old_char] == 0:
                del s_count[old_char]

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
