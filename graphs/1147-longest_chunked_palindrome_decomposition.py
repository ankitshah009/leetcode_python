#1147. Longest Chunked Palindrome Decomposition
#Hard
#
#You are given a string text. You should split it to k substrings
#(subtext1, subtext2, ..., subtextk) such that:
#    subtexti is a non-empty string.
#    The concatenation of all the substrings is equal to text
#    (i.e., subtext1 + subtext2 + ... + subtextk == text).
#    subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
#
#Return the largest possible value of k.
#
#Example 1:
#Input: text = "ghiabcdefhelloadamhelloabcdefghi"
#Output: 7
#Explanation: We can split the string as
#"(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
#
#Example 2:
#Input: text = "merchant"
#Output: 1
#Explanation: We can split the string as "(merchant)".
#
#Example 3:
#Input: text = "antaprezatepzapreanta"
#Output: 11
#Explanation: We can split the string as
#"(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
#
#Constraints:
#    1 <= text.length <= 1000
#    text consists only of lowercase English characters.

class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        Greedy: Match shortest prefix with suffix, recurse on middle.
        """
        n = len(text)
        if n == 0:
            return 0

        for i in range(1, n // 2 + 1):
            if text[:i] == text[n - i:]:
                # Found match, recurse on middle
                return 2 + self.longestDecomposition(text[i:n - i])

        # No match found, entire string is one chunk
        return 1


class SolutionIterative:
    def longestDecomposition(self, text: str) -> int:
        """Iterative two-pointer approach"""
        n = len(text)
        left, right = 0, n - 1
        count = 0
        left_str, right_str = "", ""

        while left < right:
            left_str += text[left]
            right_str = text[right] + right_str

            if left_str == right_str:
                count += 2
                left_str = right_str = ""

            left += 1
            right -= 1

        # Handle middle part
        if left == right or left_str:
            count += 1

        return count


class SolutionHash:
    def longestDecomposition(self, text: str) -> int:
        """Rolling hash for faster string comparison"""
        n = len(text)
        if n == 0:
            return 0

        BASE = 31
        MOD = 10**9 + 7

        left, right = 0, n - 1
        count = 0
        left_hash, right_hash = 0, 0
        power = 1

        while left < right:
            left_hash = (left_hash * BASE + ord(text[left]) - ord('a') + 1) % MOD
            right_hash = (right_hash + (ord(text[right]) - ord('a') + 1) * power) % MOD
            power = power * BASE % MOD

            if left_hash == right_hash and text[:left + 1] == text[right:]:
                count += 2
                left_hash = right_hash = 0
                power = 1

            left += 1
            right -= 1

        if left == right or left_hash:
            count += 1

        return count
