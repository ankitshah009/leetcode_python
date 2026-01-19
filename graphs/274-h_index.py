#274. H-Index
#Medium
#
#Given an array of integers citations where citations[i] is the number of
#citations a researcher received for their ith paper, return the researcher's
#h-index.
#
#According to the definition of h-index on Wikipedia: The h-index is defined as
#the maximum value of h such that the given researcher has published at least h
#papers that have each been cited at least h times.
#
#Example 1:
#Input: citations = [3,0,6,1,5]
#Output: 3
#Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of
#them had received 3, 0, 6, 1, 5 citations respectively.
#Since the researcher has 3 papers with at least 3 citations each and the
#remaining two with no more than 3 citations each, their h-index is 3.
#
#Example 2:
#Input: citations = [1,3,1]
#Output: 1
#
#Constraints:
#    n == citations.length
#    1 <= n <= 5000
#    0 <= citations[i] <= 1000

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Sort and find h-index - O(n log n)"""
        citations.sort(reverse=True)

        h = 0
        for i, c in enumerate(citations):
            # i+1 papers have at least c citations
            if c >= i + 1:
                h = i + 1
            else:
                break

        return h


class SolutionCounting:
    """Counting sort approach - O(n) time"""

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # Count papers with each citation count
        # Papers with > n citations are treated as n
        counts = [0] * (n + 1)

        for c in citations:
            counts[min(c, n)] += 1

        # Count from high to low
        total = 0
        for h in range(n, -1, -1):
            total += counts[h]
            # If total papers with at least h citations >= h
            if total >= h:
                return h

        return 0


class SolutionBinarySearch:
    """Binary search after sorting"""

    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            papers_with_at_least = n - mid  # Number of papers with at least citations[mid]

            if citations[mid] >= papers_with_at_least:
                right = mid - 1
            else:
                left = mid + 1

        return n - left
