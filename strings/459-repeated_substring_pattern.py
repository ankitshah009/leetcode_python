#459. Repeated Substring Pattern
#Easy
#
#Given a string s, check if it can be constructed by taking a substring of it and appending
#multiple copies of the substring together.
#
#Example 1:
#Input: s = "abab"
#Output: true
#Explanation: It is the substring "ab" twice.
#
#Example 2:
#Input: s = "aba"
#Output: false
#
#Example 3:
#Input: s = "abcabcabcabc"
#Output: true
#Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # If s can be formed by repeating a substring, then s will be found in (s + s)[1:-1]
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern_check(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                pattern = s[:length]
                if pattern * (n // length) == s:
                    return True
        return False
