#1374. Generate a String With Characters That Have Odd Counts
#Easy
#
#Given an integer n, return a string with n characters such that each character
#in such string occurs an odd number of times.
#
#The returned string must contain only lowercase English letters. If there are
#multiple valid strings, return any of them.
#
#Example 1:
#Input: n = 4
#Output: "pppz"
#Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
#
#Example 2:
#Input: n = 2
#Output: "xy"
#Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
#
#Example 3:
#Input: n = 7
#Output: "holasss"
#
#Constraints:
#    1 <= n <= 500

class Solution:
    def generateTheString(self, n: int) -> str:
        """
        If n is odd: return n 'a's (one character, odd count)
        If n is even: return (n-1) 'a's + 1 'b' (both odd counts)
        """
        if n % 2 == 1:
            return 'a' * n
        return 'a' * (n - 1) + 'b'


class SolutionAlternative:
    def generateTheString(self, n: int) -> str:
        """Alternative one-liner"""
        return 'a' * (n - 1) + ('a' if n % 2 else 'b')
