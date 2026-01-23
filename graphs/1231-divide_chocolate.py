#1231. Divide Chocolate
#Hard
#
#You have one chocolate bar that consists of some chunks. Each chunk has its
#own sweetness given by the array sweetness.
#
#You want to share the chocolate with your k friends so you start cutting the
#chocolate bar into k + 1 pieces using k cuts, each piece consists of some
#consecutive chunks.
#
#Being generous, you will eat the piece with the minimum total sweetness and
#give the other pieces to your friends.
#
#Find the maximum total sweetness of the piece you can get by cutting the
#chocolate bar optimally.
#
#Example 1:
#Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
#Output: 6
#Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
#
#Example 2:
#Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
#Output: 1
#Explanation: There is only one way to cut the bar into 9 pieces.
#
#Example 3:
#Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
#Output: 5
#Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
#
#Constraints:
#    0 <= k < sweetness.length <= 10^4
#    1 <= sweetness[i] <= 10^5

from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """
        Binary search on the answer (minimum sweetness you can get).
        For a given minimum sweetness, check if we can make k+1 pieces
        where each piece has at least that sweetness.
        """
        def can_divide(min_sweetness):
            """Can we divide into k+1 pieces, each with at least min_sweetness?"""
            pieces = 0
            current = 0

            for s in sweetness:
                current += s
                if current >= min_sweetness:
                    pieces += 1
                    current = 0

            return pieces >= k + 1

        # Binary search
        left = min(sweetness)
        right = sum(sweetness) // (k + 1)

        while left < right:
            mid = (left + right + 1) // 2  # Round up

            if can_divide(mid):
                left = mid  # Try for higher minimum
            else:
                right = mid - 1

        return left


class SolutionAlt:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        """Alternative binary search implementation"""
        total = sum(sweetness)
        pieces = k + 1

        left, right = 1, total // pieces

        while left <= right:
            mid = (left + right) // 2

            # Count pieces with at least mid sweetness
            count = 0
            current = 0
            for s in sweetness:
                current += s
                if current >= mid:
                    count += 1
                    current = 0

            if count >= pieces:
                left = mid + 1
            else:
                right = mid - 1

        return right
