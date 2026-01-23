#9. Palindrome Number
#Easy
#
#Given an integer x, return true if x is a palindrome, and false otherwise.
#
#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#
#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes
#121-. Therefore it is not a palindrome.
#
#Example 3:
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#Constraints:
#    -2^31 <= x <= 2^31 - 1
#
#Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Reverse half of the number and compare.
        """
        # Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd length, we can ignore the middle digit
        return x == reversed_half or x == reversed_half // 10


class SolutionFullReverse:
    def isPalindrome(self, x: int) -> bool:
        """
        Reverse the entire number.
        """
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num


class SolutionString:
    def isPalindrome(self, x: int) -> bool:
        """
        Convert to string and compare.
        """
        s = str(x)
        return s == s[::-1]


class SolutionTwoPointers:
    def isPalindrome(self, x: int) -> bool:
        """
        Two pointers on string representation.
        """
        if x < 0:
            return False

        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
