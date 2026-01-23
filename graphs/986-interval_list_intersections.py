#986. Interval List Intersections
#Medium
#
#You are given two lists of closed intervals, firstList and secondList, where
#firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of
#intervals is pairwise disjoint and in sorted order.
#
#Return the intersection of these two interval lists.
#
#A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
#a <= x <= b.
#
#The intersection of two closed intervals is a set of real numbers that is
#either empty, or represented as a closed interval.
#
#Example 1:
#Input: firstList = [[0,2],[5,10],[13,23],[24,25]],
#       secondList = [[1,5],[8,12],[15,24],[25,26]]
#Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#Example 2:
#Input: firstList = [[1,3],[5,9]], secondList = []
#Output: []
#
#Constraints:
#    0 <= firstList.length, secondList.length <= 1000
#    firstList.length + secondList.length >= 1
#    0 <= starti < endi <= 10^9
#    0 <= startj < endj <= 10^9

class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        """
        Two pointer approach.
        """
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            # Find intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            # Move pointer of interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result


class SolutionExplicit:
    """More explicit overlap check"""

    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        result = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Check if overlapping
            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])

            # Advance the one that ends earlier
            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return result
