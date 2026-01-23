#1750. Minimum Length of String After Deleting Similar Ends
#Medium
#
#Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked
#to apply the following algorithm on the string any number of times:
#
#1. Pick a non-empty prefix from the string s where all the characters in the
#   prefix are equal.
#2. Pick a non-empty suffix from the string s where all the characters in the
#   suffix are equal.
#3. The prefix and the suffix should not intersect at any index.
#4. The characters from the prefix and suffix must be the same.
#5. Delete both the prefix and the suffix.
#
#Return the minimum length of s after performing the above operation any number
#of times (possibly zero times).
#
#Example 1:
#Input: s = "ca"
#Output: 2
#
#Example 2:
#Input: s = "cabaabac"
#Output: 0
#
#Example 3:
#Input: s = "aabccabba"
#Output: 3
#
#Constraints:
#    1 <= s.length <= 10^5
#    s only consists of characters 'a', 'b', and 'c'.

class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Two pointers from both ends.
        """
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]

            # Skip all matching characters from left
            while left <= right and s[left] == char:
                left += 1

            # Skip all matching characters from right
            while left <= right and s[right] == char:
                right -= 1

        return right - left + 1


class SolutionRecursive:
    def minimumLength(self, s: str) -> int:
        """
        Recursive approach.
        """
        def helper(left: int, right: int) -> int:
            if left >= right:
                return right - left + 1 if left == right else 0

            if s[left] != s[right]:
                return right - left + 1

            char = s[left]

            # Skip matching characters
            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1

            return helper(left, right)

        return helper(0, len(s) - 1)


class SolutionWhile:
    def minimumLength(self, s: str) -> int:
        """
        Alternative while loop structure.
        """
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                break

            c = s[i]

            while i <= j and s[i] == c:
                i += 1

            while j >= i and s[j] == c:
                j -= 1

        return max(0, j - i + 1)
