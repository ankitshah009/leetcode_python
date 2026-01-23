#717. 1-bit and 2-bit Characters
#Easy
#
#We have two special characters:
#- The first character can be represented by one bit 0.
#- The second character can be represented by two bits (10 or 11).
#
#Given a binary array bits that ends with 0, return true if the last character
#must be a one-bit character.
#
#Example 1:
#Input: bits = [1,0,0]
#Output: true
#Explanation: The only way to decode it is two-bit character (10) and one-bit
#character (0). So the last character is one-bit character.
#
#Example 2:
#Input: bits = [1,1,1,0]
#Output: false
#Explanation: The only way to decode it is two-bit character (11) and two-bit
#character (10). So the last character is NOT one-bit character.
#
#Constraints:
#    1 <= bits.length <= 1000
#    bits[i] is either 0 or 1.

class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        Greedy: decode from left to right.
        If 1, skip next bit (2-bit char). If 0, it's 1-bit char.
        """
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2  # 2-bit character
            else:
                i += 1  # 1-bit character

        return i == n - 1  # Ended exactly at last position


class SolutionCountOnes:
    """
    Count consecutive 1s before the last 0.
    If odd number of 1s, last 0 is part of 2-bit char.
    """

    def isOneBitCharacter(self, bits: list[int]) -> bool:
        # Count 1s right before the last 0
        count = 0
        i = len(bits) - 2

        while i >= 0 and bits[i] == 1:
            count += 1
            i -= 1

        return count % 2 == 0


class SolutionDP:
    """DP approach to check if valid decode exists"""

    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)

        # dp[i] = True if bits[i:] can start a valid decode
        # AND last char is 1-bit
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            if bits[i] == 0:
                # 1-bit character, check remaining
                dp[i] = dp[i + 1]
            else:
                # Must be 2-bit character
                if i + 2 <= n:
                    dp[i] = dp[i + 2]

        # Check specifically if last char is 1-bit
        # Reset and check ending condition
        i = 0
        while i < n - 1:
            i += 2 if bits[i] == 1 else 1

        return i == n - 1
