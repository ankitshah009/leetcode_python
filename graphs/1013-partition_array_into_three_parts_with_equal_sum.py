#1013. Partition Array Into Three Parts With Equal Sum
#Easy
#
#Given an array of integers arr, return true if we can partition the array into
#three non-empty parts with equal sums.
#
#Formally, we can partition the array if we can find indexes i + 1 < j with:
#arr[0] + arr[1] + ... + arr[i] ==
#arr[i + 1] + arr[i + 2] + ... + arr[j - 1] ==
#arr[j] + arr[j + 1] + ... + arr[arr.length - 1]
#
#Example 1:
#Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
#Output: true
#Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#Example 2:
#Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
#Output: false
#
#Example 3:
#Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
#Output: true
#Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#Constraints:
#    3 <= arr.length <= 5 * 10^4
#    -10^4 <= arr[i] <= 10^4

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        """
        Find two split points where prefix sums equal total/3.
        """
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        prefix_sum = 0
        count = 0

        for i in range(len(arr) - 1):  # Leave at least 1 element for last part
            prefix_sum += arr[i]

            if prefix_sum == target * (count + 1):
                count += 1
                if count == 2:
                    return True

        return False


class SolutionTwoPointers:
    """Two pointers approach"""

    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        n = len(arr)

        # Find first split
        prefix = 0
        i = 0
        while i < n - 2:
            prefix += arr[i]
            if prefix == target:
                break
            i += 1
        else:
            return False

        # Find second split
        middle = 0
        j = i + 1
        while j < n - 1:
            middle += arr[j]
            if middle == target:
                return True
            j += 1

        return False


class SolutionExplicit:
    """More explicit checking"""

    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        prefix = 0
        parts = 0

        for i, num in enumerate(arr):
            prefix += num
            if prefix == target * (parts + 1) and i < len(arr) - 1:
                parts += 1

        return parts >= 2
