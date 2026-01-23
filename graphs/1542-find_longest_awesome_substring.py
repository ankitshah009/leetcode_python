#1542. Find Longest Awesome Substring
#Hard
#
#You are given a string s. An awesome substring is a non-empty substring of s
#such that we can make any number of swaps in order to make it a palindrome.
#
#Return the length of the maximum length awesome substring of s.
#
#Example 1:
#Input: s = "3242415"
#Output: 5
#Explanation: "24241" is the longest awesome substring, we can form the palindrome
#"24142" with some swaps.
#
#Example 2:
#Input: s = "12345678"
#Output: 1
#
#Example 3:
#Input: s = "213123"
#Output: 6
#Explanation: "213123" is the longest awesome substring, we can form the palindrome
#"231132" with some swaps.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists only of digits.

class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        A string can be rearranged into a palindrome if at most one character
        has an odd count.

        Use bitmask to track parity of digit counts.
        For substring [i, j] to be awesome:
        - XOR of masks from 0 to i-1 and 0 to j should have at most 1 bit set.

        This means: mask[j] XOR mask[i-1] has at most 1 bit set.
        - Equal masks (XOR = 0): all counts even
        - Differ by one bit: exactly one odd count
        """
        # First occurrence of each mask
        first_occurrence = {0: -1}

        mask = 0
        max_len = 0

        for i, c in enumerate(s):
            digit = int(c)
            mask ^= (1 << digit)

            # Check if same mask seen before (all even counts)
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i

            # Check masks that differ by exactly one bit
            for d in range(10):
                prev_mask = mask ^ (1 << d)
                if prev_mask in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prev_mask])

        return max_len


class SolutionArray:
    def longestAwesome(self, s: str) -> int:
        """
        Using array instead of dict for faster lookup.
        Mask can be 0 to 2^10 - 1 = 1023.
        """
        # First occurrence of each mask (-2 means not seen)
        first = [-2] * 1024
        first[0] = -1

        mask = 0
        result = 0

        for i, c in enumerate(s):
            mask ^= (1 << int(c))

            # Same mask
            if first[mask] != -2:
                result = max(result, i - first[mask])
            else:
                first[mask] = i

            # Differ by one bit
            for d in range(10):
                prev = mask ^ (1 << d)
                if first[prev] != -2:
                    result = max(result, i - first[prev])

        return result


class SolutionExplained:
    def longestAwesome(self, s: str) -> int:
        """
        Detailed explanation with step-by-step logic.

        For a string to be rearrangeable into a palindrome:
        - If even length: all chars must have even count
        - If odd length: exactly one char has odd count

        Bitmask approach:
        - Bit d is set if digit d has odd count in prefix
        - For substring s[i:j+1], the mask is prefix[j+1] XOR prefix[i]
        - We want this XOR to be 0 (all even) or have exactly one bit set (one odd)
        """
        n = len(s)

        # Map from mask to earliest index where this mask occurs
        seen = {0: -1}

        prefix_mask = 0
        best = 0

        for idx in range(n):
            digit = ord(s[idx]) - ord('0')
            prefix_mask ^= (1 << digit)

            # Case 1: Same mask seen before
            if prefix_mask in seen:
                best = max(best, idx - seen[prefix_mask])
            else:
                seen[prefix_mask] = idx

            # Case 2: Mask differs by exactly one bit
            for bit in range(10):
                target = prefix_mask ^ (1 << bit)
                if target in seen:
                    best = max(best, idx - seen[target])

        return best


class SolutionBruteForce:
    def longestAwesome(self, s: str) -> int:
        """
        Brute force (for verification, O(n^2) - will TLE on large inputs).
        """
        n = len(s)
        best = 1

        def can_form_palindrome(substring):
            from collections import Counter
            counts = Counter(substring)
            odd_count = sum(1 for c in counts.values() if c % 2 == 1)
            return odd_count <= 1

        for i in range(n):
            for j in range(i + best, n):
                if can_form_palindrome(s[i:j + 1]):
                    best = j - i + 1

        return best
