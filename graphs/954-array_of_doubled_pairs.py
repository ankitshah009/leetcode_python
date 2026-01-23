#954. Array of Doubled Pairs
#Medium
#
#Given an integer array of even length arr, return true if it is possible to
#reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2,
#or false otherwise.
#
#Example 1:
#Input: arr = [3,1,3,6]
#Output: false
#
#Example 2:
#Input: arr = [2,1,2,6]
#Output: false
#
#Example 3:
#Input: arr = [4,-2,2,-4]
#Output: true
#Explanation: We can take two groups: [-2,-4] and [2,4].
#
#Constraints:
#    2 <= arr.length <= 3 * 10^4
#    arr.length is even.
#    -10^5 <= arr[i] <= 10^5

from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        """
        Greedy: process by absolute value, pair each with its double.
        """
        count = Counter(arr)

        # Sort by absolute value
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]

        return True


class SolutionExplicit:
    """More explicit pairing"""

    def canReorderDoubled(self, arr: list[int]) -> bool:
        count = Counter(arr)

        # Handle zero separately
        if count[0] % 2 != 0:
            return False

        # Process positive and negative separately
        positives = sorted([x for x in count if x > 0])
        negatives = sorted([x for x in count if x < 0], reverse=True)

        def can_pair(nums):
            for x in nums:
                if count[x] == 0:
                    continue
                if count[2 * x] < count[x]:
                    return False
                count[2 * x] -= count[x]
                count[x] = 0
            return True

        return can_pair(positives) and can_pair(negatives)


class SolutionSortAll:
    """Sort by absolute value and pair"""

    def canReorderDoubled(self, arr: list[int]) -> bool:
        count = Counter(arr)

        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            count[x] -= 1
            count[2 * x] -= 1

        return True
