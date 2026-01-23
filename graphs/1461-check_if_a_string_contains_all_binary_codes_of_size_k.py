#1461. Check If a String Contains All Binary Codes of Size K
#Medium
#
#Given a binary string s and an integer k, return true if every binary code
#of length k is a substring of s. Otherwise, return false.
#
#Example 1:
#Input: s = "00110110", k = 2
#Output: true
#Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
#They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
#
#Example 2:
#Input: s = "0110", k = 1
#Output: true
#Explanation: The binary codes of length 1 are "0" and "1", it is clear that
#both exist as a substring.
#
#Example 3:
#Input: s = "0110", k = 2
#Output: false
#Explanation: The binary code "00" is of length 2 and does not exist in the array.
#
#Constraints:
#    1 <= s.length <= 5 * 10^5
#    s[i] is either '0' or '1'.
#    1 <= k <= 20

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Collect all unique substrings of length k.
        Need exactly 2^k unique substrings.
        """
        if len(s) < k:
            return False

        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])

        return len(seen) == (1 << k)  # 2^k


class SolutionRollingHash:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Use rolling hash to avoid string slicing overhead.
        Treat substring as binary number.
        """
        if len(s) < k:
            return False

        need = 1 << k  # 2^k codes needed
        seen = [False] * need
        count = 0

        # Build initial hash
        hash_val = 0
        for i in range(k):
            hash_val = hash_val * 2 + (1 if s[i] == '1' else 0)

        if not seen[hash_val]:
            seen[hash_val] = True
            count += 1

        # Roll through string
        mask = (1 << k) - 1  # Mask to keep only k bits

        for i in range(k, len(s)):
            # Remove leftmost bit, add new rightmost bit
            hash_val = ((hash_val << 1) | (1 if s[i] == '1' else 0)) & mask

            if not seen[hash_val]:
                seen[hash_val] = True
                count += 1

                # Early termination
                if count == need:
                    return True

        return count == need


class SolutionBitset:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """Using integer as bitset for O(1) lookup"""
        if len(s) < k:
            return False

        need = 1 << k
        seen = 0  # Use integer as bitset
        count = 0

        hash_val = int(s[:k], 2)
        seen |= (1 << hash_val)
        count = 1

        mask = need - 1

        for i in range(k, len(s)):
            hash_val = ((hash_val << 1) | int(s[i])) & mask

            if not (seen & (1 << hash_val)):
                seen |= (1 << hash_val)
                count += 1

                if count == need:
                    return True

        return count == need
