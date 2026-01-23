#1177. Can Make Palindrome from Substring
#Medium
#
#You are given a string s and array queries where queries[i] = [lefti, righti, ki].
#We may rearrange the substring s[lefti...righti] for each query and then choose
#up to ki of them to replace with any lowercase English letter.
#
#If the substring is possible to be a palindrome string after the operations
#above, the result of the query is true. Otherwise, the result is false.
#
#Return a boolean array answer where answer[i] is the result of the ith query.
#
#Example 1:
#Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
#Output: [true,false,false,true,true]
#
#Example 2:
#Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
#Output: [false,true]
#
#Constraints:
#    1 <= s.length, queries.length <= 10^5
#    0 <= lefti <= righti < s.length
#    0 <= ki <= s.length
#    s consists of lowercase English letters.

from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """
        Key insight: A string can be rearranged into palindrome if at most
        one char has odd frequency.

        With k replacements, we can fix k pairs of odd-frequency chars.
        So we need: (odd_count) // 2 <= k

        Use prefix sum with bitmask to track odd/even frequencies.
        """
        n = len(s)

        # prefix[i] = bitmask of chars with odd frequency in s[0:i]
        prefix = [0] * (n + 1)

        for i in range(n):
            char_bit = 1 << (ord(s[i]) - ord('a'))
            prefix[i + 1] = prefix[i] ^ char_bit

        result = []
        for left, right, k in queries:
            # XOR gives chars with odd frequency in s[left:right+1]
            xor = prefix[right + 1] ^ prefix[left]

            # Count set bits (chars with odd frequency)
            odd_count = bin(xor).count('1')

            # We can fix odd_count // 2 pairs with k replacements
            result.append(odd_count // 2 <= k)

        return result


class SolutionArray:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """Using array prefix sum instead of bitmask"""
        n = len(s)

        # prefix[i][c] = count of char c in s[0:i]
        prefix = [[0] * 26 for _ in range(n + 1)]

        for i in range(n):
            for c in range(26):
                prefix[i + 1][c] = prefix[i][c]
            prefix[i + 1][ord(s[i]) - ord('a')] += 1

        result = []
        for left, right, k in queries:
            # Count chars with odd frequency
            odd_count = 0
            for c in range(26):
                count = prefix[right + 1][c] - prefix[left][c]
                if count % 2 == 1:
                    odd_count += 1

            result.append(odd_count // 2 <= k)

        return result
