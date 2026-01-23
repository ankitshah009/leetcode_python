#1332. Remove Palindromic Subsequences
#Easy
#
#You are given a string s consisting only of letters 'a' and 'b'. In a single
#step you can remove one palindromic subsequence from s.
#
#Return the minimum number of steps to make the given string empty.
#
#A subsequence of a string is a sequence that can be derived from the given
#string by deleting some or no elements without changing the order of the
#remaining elements.
#
#A string is called palindrome if it reads the same backward as forward.
#
#Example 1:
#Input: s = "ababa"
#Output: 1
#Explanation: s is already a palindrome, so its entire is removed in a single step.
#
#Example 2:
#Input: s = "abb"
#Output: 2
#Explanation: "abb" -> "bb" -> "".
#Remove palindromic subsequence "a" then "bb".
#
#Example 3:
#Input: s = "baabb"
#Output: 2
#Explanation: "baabb" -> "b" -> "".
#Remove palindromic subsequence "baab" then "b".
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either 'a' or 'b'.

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        Key insight: Since string only has 'a' and 'b':
        - If s is empty: 0 steps
        - If s is palindrome: 1 step (remove entire string)
        - Otherwise: 2 steps (remove all 'a's, then all 'b's)

        All 'a's form a palindrome ("aaa..."), all 'b's form a palindrome ("bbb...")
        """
        if not s:
            return 0

        if s == s[::-1]:
            return 1

        return 2


class SolutionExplicit:
    def removePalindromeSub(self, s: str) -> int:
        """More explicit palindrome check"""
        if not s:
            return 0

        # Check if palindrome
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1

        return 1
