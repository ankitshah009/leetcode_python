#541. Reverse String II
#Easy
#
#Given a string s and an integer k, reverse the first k characters for every 2k
#characters counting from the start of the string.
#
#If there are fewer than k characters left, reverse all of them. If there are less
#than 2k but greater than or equal to k characters, then reverse the first k
#characters and leave the other as original.
#
#Example 1:
#Input: s = "abcdefg", k = 2
#Output: "bacdfeg"
#
#Example 2:
#Input: s = "abcd", k = 2
#Output: "bacd"
#
#Constraints:
#    1 <= s.length <= 10^4
#    s consists of only lowercase English letters.
#    1 <= k <= 10^4

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """Process in chunks of 2k"""
        chars = list(s)

        for i in range(0, len(s), 2 * k):
            # Reverse first k characters of this chunk
            left, right = i, min(i + k - 1, len(s) - 1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)


class SolutionSlicing:
    """Using string slicing"""

    def reverseStr(self, s: str, k: int) -> str:
        result = []

        for i in range(0, len(s), 2 * k):
            chunk = s[i:i + 2*k]
            # Reverse first k characters
            result.append(chunk[:k][::-1] + chunk[k:])

        return ''.join(result)


class SolutionCompact:
    """Compact one-liner approach"""

    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(
            s[i:i+k][::-1] + s[i+k:i+2*k]
            for i in range(0, len(s), 2*k)
        )
