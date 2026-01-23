#1925. Count Square Sum Triples
#Easy
#
#A square triple (a,b,c) is a triple where a, b, and c are integers and
#a^2 + b^2 = c^2.
#
#Given an integer n, return the number of square triples such that
#1 <= a, b, c <= n.
#
#Example 1:
#Input: n = 5
#Output: 2
#Explanation: (3, 4, 5) and (4, 3, 5)
#
#Example 2:
#Input: n = 10
#Output: 4
#Explanation: (3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)
#
#Constraints:
#    1 <= n <= 250

class Solution:
    def countTriples(self, n: int) -> int:
        """
        Check all pairs (a, b) and see if c = sqrt(a^2 + b^2) is valid.
        """
        count = 0
        squares = {i * i for i in range(1, n + 1)}

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_sq = a * a + b * b
                if c_sq in squares:
                    count += 1

        return count


class SolutionOptimized:
    def countTriples(self, n: int) -> int:
        """
        Only check a <= b to avoid duplicate work, then multiply by 2.
        """
        import math

        count = 0

        for a in range(1, n + 1):
            for b in range(a, n + 1):  # b >= a
                c_sq = a * a + b * b
                c = int(math.sqrt(c_sq))

                if c <= n and c * c == c_sq:
                    # (a, b, c) is valid
                    if a == b:
                        count += 1  # Only one ordering
                    else:
                        count += 2  # Both (a, b, c) and (b, a, c)

        return count


class SolutionBruteForce:
    def countTriples(self, n: int) -> int:
        """
        Check all triples directly.
        """
        count = 0

        for c in range(1, n + 1):
            c_sq = c * c
            for a in range(1, c):
                for b in range(1, c):
                    if a * a + b * b == c_sq:
                        count += 1

        return count
