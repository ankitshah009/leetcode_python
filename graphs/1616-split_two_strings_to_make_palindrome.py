#1616. Split Two Strings to Make Palindrome
#Medium
#
#You are given two strings a and b of the same length. Choose an index and
#split both strings at the same index, splitting a into two strings:
#aprefix and asuffix where a = aprefix + asuffix, and splitting b into two
#strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if
#aprefix + bsuffix or bprefix + asuffix forms a palindrome.
#
#When you split a string s into sprefix and ssuffix, either ssuffix or sprefix
#is allowed to be empty. For example, if s = "abc", then "" + "abc",
#"a" + "bc", "ab" + "c", and "abc" + "" are valid splits.
#
#Return true if it is possible to form a palindrome string, otherwise return false.
#
#Notice that x + y denotes the concatenation of strings x and y.
#
#Example 1:
#Input: a = "x", b = "y"
#Output: true
#Explanation: If either a or b are palindromes the answer is true.
#Here aprefix = "", asuffix = "x", bprefix = "", bsuffix = "y".
#aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
#
#Example 2:
#Input: a = "xbdef", b = "xecab"
#Output: false
#
#Example 3:
#Input: a = "ulacfd", b = "jizalu"
#Output: true
#Explanation: Split them at index 3:
#aprefix = "ula", asuffix = "cfd", bprefix = "jiz", bsuffix = "alu".
#aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
#
#Constraints:
#    1 <= a.length, b.length <= 10^5
#    a.length == b.length
#    a and b consist of lowercase English letters

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        For a_prefix + b_suffix to be palindrome:
        a[0:i] and b[n-i:n] must mirror each other at the extremes,
        and the middle portion must be a palindrome.

        Try both combinations: (a prefix + b suffix) and (b prefix + a suffix)
        """
        def check(s1: str, s2: str) -> bool:
            # Check if prefix of s1 + suffix of s2 can form palindrome
            n = len(s1)
            i, j = 0, n - 1

            # Match s1 prefix with s2 suffix
            while i < j and s1[i] == s2[j]:
                i += 1
                j -= 1

            # Now check if middle is palindrome in either string
            return is_palindrome(s1, i, j) or is_palindrome(s2, i, j)

        def is_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        return check(a, b) or check(b, a)


class SolutionDetailed:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        Detailed solution with explanation.

        For a_prefix + b_suffix to be palindrome:
        1. The outer characters must match: a[0] == b[-1], a[1] == b[-2], etc.
        2. At some point, we switch to checking if middle portion is palindrome.

        Two cases:
        - Continue matching outer chars, then check middle of a
        - Continue matching outer chars, then check middle of b
        """
        n = len(a)

        def helper(s1: str, s2: str) -> bool:
            # Try s1_prefix + s2_suffix
            left, right = 0, n - 1

            # Greedily match outer characters
            while left < right and s1[left] == s2[right]:
                left += 1
                right -= 1

            # Check if remaining middle is palindrome in either string
            # Middle of s1: s1[left:right+1]
            # Middle of s2: s2[left:right+1]

            def is_palindrome(s, l, r):
                while l < r:
                    if s[l] != s[r]:
                        return False
                    l += 1
                    r -= 1
                return True

            return is_palindrome(s1, left, right) or is_palindrome(s2, left, right)

        return helper(a, b) or helper(b, a)


class SolutionBruteForce:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        Brute force: try all split points.
        O(n^2) - will TLE for large inputs but demonstrates the idea.
        """
        n = len(a)

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        for i in range(n + 1):
            if is_palindrome(a[:i] + b[i:]) or is_palindrome(b[:i] + a[i:]):
                return True

        return False
