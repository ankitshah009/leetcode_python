#1545. Find Kth Bit in Nth Binary String
#Medium
#
#Given two positive integers n and k, the binary string Sn is formed as follows:
#- S1 = "0"
#- Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
#
#Where + denotes the concatenation operation, reverse(x) returns the reversed
#string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
#
#For example, the first four strings in the above sequence are:
#- S1 = "0"
#- S2 = "011"
#- S3 = "0111001"
#- S4 = "011100110110001"
#
#Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
#
#Example 1:
#Input: n = 3, k = 1
#Output: "0"
#Explanation: S3 is "0111001". The 1st bit is "0".
#
#Example 2:
#Input: n = 4, k = 11
#Output: "1"
#Explanation: S4 is "011100110110001". The 11th bit is "1".
#
#Example 3:
#Input: n = 1, k = 1
#Output: "0"
#
#Example 4:
#Input: n = 2, k = 3
#Output: "1"
#
#Constraints:
#    1 <= n <= 20
#    1 <= k <= 2^n - 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Recursive approach based on string structure.

        Length of S_n = 2^n - 1
        S_n = S_{n-1} + "1" + reverse(invert(S_{n-1}))

        For position k in S_n:
        - If k < mid: answer is in S_{n-1} at position k
        - If k == mid: answer is "1"
        - If k > mid: answer is inverted from S_{n-1} at position (len - k + 1)
        """
        length = (1 << n) - 1  # 2^n - 1
        mid = (length + 1) // 2  # Middle position

        if n == 1:
            return "0"

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # Position in the reversed inverted part
            mirror_pos = length - k + 1
            result = self.findKthBit(n - 1, mirror_pos)
            return "1" if result == "0" else "0"


class SolutionIterative:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Iterative version tracking inversions.
        """
        invert_count = 0

        while n > 1:
            length = (1 << n) - 1
            mid = (length + 1) // 2

            if k == mid:
                return "1" if invert_count % 2 == 0 else "0"
            elif k > mid:
                # Mirror position
                k = length - k + 1
                invert_count += 1

            n -= 1

        # n == 1, k == 1, S1 = "0"
        return "0" if invert_count % 2 == 0 else "1"


class SolutionBuild:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Build the string (only works for small n).
        """
        s = "0"

        for _ in range(n - 1):
            inverted = ''.join('1' if c == '0' else '0' for c in s)
            s = s + '1' + inverted[::-1]

        return s[k - 1]


class SolutionBitwise:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Using bit manipulation for the recursive descent.
        """
        flip = 0

        while k > 1:
            length = (1 << n) - 1
            mid = length // 2 + 1

            if k == mid:
                return '0' if flip else '1'
            elif k > mid:
                k = length - k + 1
                flip ^= 1

            n -= 1

        return str(flip)


class SolutionMath:
    def findKthBit(self, n: int, k: int) -> str:
        """
        Mathematical pattern observation.

        For position k (1-indexed):
        - Count how many times k falls into the "right half"
        - This determines the inversion count
        """
        inversions = 0

        while True:
            length = (1 << n) - 1
            mid = (length + 1) // 2

            if k == mid:
                return '1' if inversions % 2 == 0 else '0'
            elif k > mid:
                k = length - k + 1
                inversions += 1

            n -= 1
            if n == 0:
                break

        # Base case: k = 1 in S1 is "0"
        return '0' if inversions % 2 == 0 else '1'
