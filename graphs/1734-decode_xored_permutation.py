#1734. Decode XORed Permutation
#Medium
#
#There is an integer array perm that is a permutation of the first n positive
#integers, where n is always odd.
#
#It was encoded into another integer array encoded of length n - 1, such that
#encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then
#encoded = [2,1].
#
#Given the encoded array, return the original array perm. It is guaranteed that
#the answer exists and is unique.
#
#Example 1:
#Input: encoded = [3,1]
#Output: [1,2,3]
#
#Example 2:
#Input: encoded = [6,5,4,6]
#Output: [2,4,1,5,3]
#
#Constraints:
#    3 <= n < 10^5
#    n is odd.
#    encoded.length == n - 1

from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        """
        Key insight: We know XOR of all 1 to n.
        encoded[1] ^ encoded[3] ^ ... = perm[2] ^ perm[3] ^ ... ^ perm[n]
        XOR of 1 to n minus above gives perm[1].
        """
        n = len(encoded) + 1

        # XOR of all numbers from 1 to n
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i

        # XOR of encoded[1], encoded[3], encoded[5], ...
        # This equals perm[2] ^ perm[3] ^ ... ^ perm[n]
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]

        # perm[0] = total_xor ^ odd_xor
        first = total_xor ^ odd_xor

        # Decode the rest
        result = [first]
        for enc in encoded:
            result.append(result[-1] ^ enc)

        return result


class SolutionExplained:
    def decode(self, encoded: List[int]) -> List[int]:
        """
        More detailed explanation of the approach.
        """
        n = len(encoded) + 1

        # perm is [1, 2, 3, ..., n] in some order
        # XOR of 1 to n = 1 ^ 2 ^ 3 ^ ... ^ n
        xor_all = 0
        for i in range(1, n + 1):
            xor_all ^= i

        # encoded[0] = perm[0] ^ perm[1]
        # encoded[1] = perm[1] ^ perm[2]
        # encoded[2] = perm[2] ^ perm[3]
        # ...

        # encoded[1] ^ encoded[3] ^ encoded[5] ^ ...
        # = (perm[1] ^ perm[2]) ^ (perm[3] ^ perm[4]) ^ ...
        # = perm[1] ^ perm[2] ^ perm[3] ^ ... ^ perm[n-1]
        # (excludes perm[0] and perm[n-1] on odd indices when n is odd)

        # Actually: encoded[1] ^ encoded[3] ^ ... = perm[2] ^ perm[n]
        # So xor_all ^ this = perm[0]

        xor_except_first = 0
        for i in range(1, len(encoded), 2):
            xor_except_first ^= encoded[i]

        first = xor_all ^ xor_except_first

        result = [first]
        for enc in encoded:
            result.append(result[-1] ^ enc)

        return result
