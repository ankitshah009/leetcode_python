#214. Shortest Palindrome
#Hard
#
#You are given a string s. You can convert s to a palindrome by adding characters
#in front of it.
#
#Return the shortest palindrome you can find by performing this transformation.
#
#Example 1:
#Input: s = "aacecaaa"
#Output: "aaacecaaa"
#
#Example 2:
#Input: s = "abcd"
#Output: "dcbabcd"
#
#Constraints:
#    0 <= s.length <= 5 * 10^4
#    s consists of lowercase English letters only.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Find the longest palindrome starting at index 0
        # Then prepend the reverse of remaining suffix

        # Use KMP failure function
        # Concatenate s + "#" + reverse(s) and find LPS
        rev = s[::-1]
        concat = s + "#" + rev

        # Build KMP failure/LPS array
        n = len(concat)
        lps = [0] * n

        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and concat[i] != concat[j]:
                j = lps[j - 1]
            if concat[i] == concat[j]:
                j += 1
            lps[i] = j

        # lps[-1] gives length of longest palindromic prefix
        longest_palindrome_prefix = lps[-1]

        # Add reverse of suffix to front
        suffix_to_add = rev[:len(s) - longest_palindrome_prefix]
        return suffix_to_add + s

    # Alternative: Two-pointer approach (less efficient but intuitive)
    def shortestPalindromeTwoPointer(self, s: str) -> str:
        if not s:
            return s

        n = len(s)
        i = 0

        # Find the longest palindromic prefix
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                i += 1

        if i == n:
            return s  # Already a palindrome

        # Suffix that needs to be reversed and prepended
        suffix = s[i:]
        return suffix[::-1] + self.shortestPalindromeTwoPointer(s[:i]) + suffix
