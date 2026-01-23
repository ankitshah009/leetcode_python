#1899. Merge Triplets to Form Target Triplet
#Medium
#
#A triplet is an array of three integers. You are given a 2D integer array
#triplets, where triplets[i] = [a_i, b_i, c_i] describes the ith triplet. You
#are also given an integer array target = [x, y, z] that describes the triplet
#you want to obtain.
#
#To obtain target, you may apply the following operation on triplets any number
#of times (possibly zero):
#- Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to
#  become [max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)].
#
#Return true if it is possible to obtain the target triplet [x, y, z] as an
#element of triplets, or false otherwise.
#
#Example 1:
#Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
#Output: true
#
#Example 2:
#Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
#Output: false
#
#Example 3:
#Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
#Output: true
#
#Constraints:
#    1 <= triplets.length <= 10^5
#    triplets[i].length == target.length == 3
#    1 <= a_i, b_i, c_i, x, y, z <= 1000

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        A triplet can contribute only if all its values <= target.
        Track which positions can reach target value.
        """
        x, y, z = target
        found = [False, False, False]

        for a, b, c in triplets:
            # Only consider triplets that don't exceed any target value
            if a <= x and b <= y and c <= z:
                if a == x:
                    found[0] = True
                if b == y:
                    found[1] = True
                if c == z:
                    found[2] = True

        return all(found)


class SolutionSet:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Using set to track which target positions are achievable.
        """
        achievable = set()

        for triplet in triplets:
            # Skip if any value exceeds target
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            # Mark positions that match target
            for i in range(3):
                if triplet[i] == target[i]:
                    achievable.add(i)

        return len(achievable) == 3


class SolutionSimulate:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Simulate merging valid triplets.
        """
        result = [0, 0, 0]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                result[0] = max(result[0], a)
                result[1] = max(result[1], b)
                result[2] = max(result[2], c)

        return result == target
