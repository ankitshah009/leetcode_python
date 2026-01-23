#888. Fair Candy Swap
#Easy
#
#Alice and Bob have a different total number of candies. You are given two
#integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of
#candies of the ith box that Alice has and bobSizes[j] is the number of candies
#of the jth box that Bob has.
#
#Since they are friends, they would like to exchange one candy box each so that
#after the exchange, they both have the same total amount of candy. The total
#amount of candy a person has is the sum of the number of candies in each box
#they have.
#
#Return an integer array answer where answer[0] is the number of candies in the
#box that Alice must exchange, and answer[1] is the number of candies in the box
#that Bob must exchange. If there are multiple answers, you may return any one
#of them. It is guaranteed that at least one answer exists.
#
#Example 1:
#Input: aliceSizes = [1,1], bobSizes = [2,2]
#Output: [1,2]
#
#Example 2:
#Input: aliceSizes = [1,2], bobSizes = [2,3]
#Output: [1,2]
#
#Example 3:
#Input: aliceSizes = [2], bobSizes = [1,3]
#Output: [2,3]
#
#Constraints:
#    1 <= aliceSizes.length, bobSizes.length <= 10^4
#    1 <= aliceSizes[i], bobSizes[j] <= 10^5
#    Alice and Bob have a different total number of candies.
#    There will be at least one valid answer for the given input.

class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        """
        If Alice gives x and receives y:
        sumA - x + y = sumB - y + x
        sumA - sumB = 2x - 2y
        y = x - (sumA - sumB) / 2
        """
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_a - sum_b) // 2

        bob_set = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]

        return []


class SolutionTwoSets:
    """Using two sets"""

    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        # After swap: sumA - a + b = sumB - b + a
        # b - a = (sumB - sumA) / 2
        delta = (sum_b - sum_a) // 2

        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)

        for a in alice_set:
            b = a + delta
            if b in bob_set:
                return [a, b]

        return []


class SolutionSorted:
    """Two pointer on sorted arrays"""

    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        aliceSizes.sort()
        bobSizes.sort()

        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        target_diff = (sum_b - sum_a) // 2

        i, j = 0, 0

        while i < len(aliceSizes) and j < len(bobSizes):
            diff = bobSizes[j] - aliceSizes[i]

            if diff == target_diff:
                return [aliceSizes[i], bobSizes[j]]
            elif diff < target_diff:
                j += 1
            else:
                i += 1

        return []
