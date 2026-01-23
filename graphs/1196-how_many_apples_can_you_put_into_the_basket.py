#1196. How Many Apples Can You Put into the Basket
#Easy
#
#You have some apples and a basket that can carry up to 5000 units of weight.
#
#Given an integer array weight where weight[i] is the weight of the ith apple,
#return the maximum number of apples you can put in the basket.
#
#Example 1:
#Input: weight = [100,200,150,1000]
#Output: 4
#Explanation: All 4 apples can be carried by the basket since their sum of
#weights is 1450.
#
#Example 2:
#Input: weight = [900,950,800,1000,700,800]
#Output: 5
#Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5.
#
#Constraints:
#    1 <= weight.length <= 10^3
#    1 <= weight[i] <= 10^3

from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        Greedy: Sort by weight, take lightest apples first.
        """
        weight.sort()
        total = 0
        count = 0

        for w in weight:
            if total + w <= 5000:
                total += w
                count += 1
            else:
                break

        return count


class SolutionCounting:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        """
        Counting sort since weights are bounded by 1000.
        """
        count = [0] * 1001

        for w in weight:
            count[w] += 1

        total = 0
        apples = 0

        for w in range(1, 1001):
            while count[w] > 0 and total + w <= 5000:
                total += w
                apples += 1
                count[w] -= 1

            if total >= 5000:
                break

        return apples
