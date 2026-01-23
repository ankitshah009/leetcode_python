#1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
#Medium
#
#A decimal number is called deci-binary if each of its digits is either 0 or 1
#without any leading zeros. For example, 101 and 1100 are deci-binary, while
#112 and 3001 are not.
#
#Given a string n that represents a positive decimal integer, return the minimum
#number of positive deci-binary numbers needed so that they sum up to n.
#
#Example 1:
#Input: n = "32"
#Output: 3
#Explanation: 10 + 11 + 11 = 32
#
#Example 2:
#Input: n = "82734"
#Output: 8
#
#Example 3:
#Input: n = "27346209830709182346"
#Output: 9
#
#Constraints:
#    1 <= n.length <= 10^5
#    n consists of only digits.
#    n does not contain any leading zeros and represents a positive integer.

class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Key insight: The answer is the maximum digit in n.
        Each deci-binary number can contribute at most 1 to each digit position.
        So we need at least max_digit deci-binary numbers.
        """
        return max(int(d) for d in n)


class SolutionInt:
    def minPartitions(self, n: str) -> int:
        """
        Using integer conversion.
        """
        return int(max(n))


class SolutionExplicit:
    def minPartitions(self, n: str) -> int:
        """
        Explicit iteration.
        """
        max_digit = 0

        for char in n:
            digit = int(char)
            max_digit = max(max_digit, digit)

            # Early termination if we find 9
            if max_digit == 9:
                break

        return max_digit


class SolutionOrd:
    def minPartitions(self, n: str) -> int:
        """
        Using ord for character comparison.
        """
        return ord(max(n)) - ord('0')


class SolutionProof:
    def minPartitions(self, n: str) -> int:
        """
        Proof: If max digit is k, we need exactly k deci-binary numbers.

        Lower bound: Each deci-binary can contribute at most 1 to any position.
        So for a digit with value k, we need at least k deci-binary numbers.

        Upper bound: We can always construct k deci-binary numbers.
        For i = 1 to k, the i-th deci-binary number has 1 in positions where
        the original digit >= i, and 0 elsewhere.
        """
        return int(max(n))


class SolutionCompact:
    def minPartitions(self, n: str) -> int:
        """
        One-liner solution.
        """
        return int(max(n))
