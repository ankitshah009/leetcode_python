#898. Bitwise ORs of Subarrays
#Medium
#
#Given an integer array arr, return the number of distinct bitwise ORs of all
#the non-empty subarrays of arr.
#
#The bitwise OR of a subarray is the bitwise OR of each integer in the subarray.
#The bitwise OR of a subarray of one integer is that integer.
#
#A subarray is a contiguous non-empty sequence of elements within an array.
#
#Example 1:
#Input: arr = [0]
#Output: 1
#
#Example 2:
#Input: arr = [1,1,2]
#Output: 3
#Explanation: Possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
#ORs are 1, 1, 2, 1, 3, 3. Unique: 1, 2, 3. Count = 3.
#
#Example 3:
#Input: arr = [1,2,4]
#Output: 6
#Explanation: ORs are 1, 2, 4, 3, 6, 7. All unique.
#
#Constraints:
#    1 <= arr.length <= 5 * 10^4
#    0 <= arr[i] <= 10^9

class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        For each position, track all possible OR values of subarrays ending there.
        Key insight: number of distinct ORs at each position is limited by bit count.
        """
        result = set()
        current = set()  # ORs of subarrays ending at current position

        for num in arr:
            # New subarrays: extend previous ones and start new one
            current = {num | x for x in current} | {num}
            result |= current

        return len(result)


class SolutionOptimized:
    """Slightly optimized version"""

    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        result = set()
        prev = set()  # Previous position's OR values

        for num in arr:
            curr = {num}
            for x in prev:
                curr.add(num | x)
            result |= curr
            prev = curr

        return len(result)


class SolutionBruteForce:
    """Brute force (for understanding)"""

    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        n = len(arr)
        result = set()

        for i in range(n):
            or_val = 0
            for j in range(i, n):
                or_val |= arr[j]
                result.add(or_val)

        return len(result)
