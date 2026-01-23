#1915. Number of Wonderful Substrings
#Medium
#
#A wonderful string is a string where at most one letter appears an odd number
#of times.
#
#Given a string word that consists of the first ten lowercase English letters
#('a' through 'j'), return the number of wonderful non-empty substrings in
#word. If the same substring appears multiple times in word, then count each
#occurrence separately.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: word = "aba"
#Output: 4
#
#Example 2:
#Input: word = "aabb"
#Output: 9
#
#Example 3:
#Input: word = "he"
#Output: 2
#
#Constraints:
#    1 <= word.length <= 10^5
#    word consists of lowercase English letters from 'a' to 'j'.

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        Bitmask for character parities.
        Substring is wonderful if XOR has 0 or 1 bits set.
        """
        # mask: bit i is 1 if character i has odd count
        # For substring [i, j], its mask = prefix[j] XOR prefix[i-1]
        # Wonderful: mask has 0 or 1 bits

        count = {0: 1}  # Count of each prefix mask
        mask = 0
        result = 0

        for c in word:
            bit = ord(c) - ord('a')
            mask ^= (1 << bit)

            # Same mask -> XOR is 0 (all even)
            result += count.get(mask, 0)

            # Masks differing by one bit -> XOR has 1 bit (one odd)
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)

            count[mask] = count.get(mask, 0) + 1

        return result


class SolutionArray:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        Using array instead of dict for counts.
        """
        # 10 letters -> 2^10 = 1024 possible masks
        count = [0] * 1024
        count[0] = 1

        mask = 0
        result = 0

        for c in word:
            mask ^= (1 << (ord(c) - ord('a')))

            # All even parities
            result += count[mask]

            # Exactly one odd parity
            for i in range(10):
                result += count[mask ^ (1 << i)]

            count[mask] += 1

        return result
