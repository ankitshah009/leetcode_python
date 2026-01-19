#275. H-Index II
#Medium
#
#Given an array of integers citations where citations[i] is the number of
#citations a researcher received for their ith paper and citations is sorted
#in ascending order, return the researcher's h-index.
#
#According to the definition of h-index on Wikipedia: The h-index is defined as
#the maximum value of h such that the given researcher has published at least h
#papers that have each been cited at least h times.
#
#You must write an algorithm that runs in logarithmic time.
#
#Example 1:
#Input: citations = [0,1,3,5,6]
#Output: 3
#Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of
#them had received 0, 1, 3, 5, 6 citations respectively.
#Since the researcher has 3 papers with at least 3 citations each and the
#remaining two with no more than 3 citations each, their h-index is 3.
#
#Example 2:
#Input: citations = [1,2,100]
#Output: 2
#
#Constraints:
#    n == citations.length
#    1 <= n <= 10^5
#    0 <= citations[i] <= 1000
#    citations is sorted in ascending order.

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Binary search - O(log n).
        Find the first position where citations[mid] >= n - mid.
        """
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            papers = n - mid  # Number of papers with at least citations[mid]

            if citations[mid] >= papers:
                right = mid - 1
            else:
                left = mid + 1

        return n - left


class SolutionLinear:
    """Linear scan from right - O(n)"""

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        for i in range(n):
            papers = n - i  # Papers with at least citations[i]
            if citations[i] >= papers:
                return papers

        return 0


class SolutionBinarySearchAlt:
    """Alternative binary search formulation"""

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # Binary search for the h-index value itself
        left, right = 0, n

        while left < right:
            mid = (left + right + 1) // 2

            # Check if at least mid papers have at least mid citations
            # The (n-mid)th paper from the start has citations[n-mid]
            if n - mid >= 0 and citations[n - mid] >= mid:
                left = mid
            else:
                right = mid - 1

        return left
