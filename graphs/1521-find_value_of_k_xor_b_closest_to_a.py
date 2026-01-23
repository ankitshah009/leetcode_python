#1521. Find a Value of a Mysterious Function Closest to Target
#Hard
#
#Winston was given the above mysterious function func. He has an integer array
#arr and an integer target and he wants to find the values l and r that make
#the value |func(arr, l, r) - target| minimum possible.
#
#Return the minimum possible value of |func(arr, l, r) - target|.
#
#Notice that func should be called with the values l and r where 0 <= l, r < arr.length.
#
#func(arr, l, r):
#    if r < l:
#        return 2**31
#    ans = arr[l]
#    for i = l + 1 to r:
#        ans = ans & arr[i]
#    return ans
#
#Example 1:
#Input: arr = [9,12,3,7,15], target = 5
#Output: 2
#Explanation: Calling func with all the pairs of [l,r] =
#[[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]],
#Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0].
#The value closest to 5 is 7 and 3, thus the minimum difference is 2.
#
#Example 2:
#Input: arr = [1000000,1000000,1000000], target = 1
#Output: 999999
#Explanation: Winston called the func with all possible values of [l,r] and he
#always got 1000000, thus the min difference is 999999.
#
#Example 3:
#Input: arr = [1,2,4,8,16], target = 0
#Output: 0
#
#Constraints:
#    1 <= arr.length <= 10^5
#    1 <= arr[i] <= 10^6
#    0 <= target <= 10^7

from typing import List

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Key insight: AND operation is monotonically decreasing or constant.
        For each right endpoint, track all possible AND values with different lefts.
        Number of distinct AND values is at most log(max_val) per right.
        """
        result = float('inf')

        # Set of AND values ending at previous position
        prev_ands = set()

        for num in arr:
            # Compute new AND values ending at current position
            # For each previous AND value, AND with current num
            # Also include just current num (single element)
            curr_ands = {num}
            for val in prev_ands:
                curr_ands.add(val & num)

            # Check distances to target
            for val in curr_ands:
                result = min(result, abs(val - target))

            prev_ands = curr_ands

        return result


class SolutionOptimized:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Optimized: AND values can only decrease (or stay same).
        At most O(log(max_val)) distinct values per position.
        """
        result = abs(arr[0] - target)
        prev_set = {arr[0]}

        for i in range(1, len(arr)):
            num = arr[i]

            # New set: current num AND with all previous, plus just current
            curr_set = {num}
            for val in prev_set:
                curr_set.add(val & num)

            # Update result
            for val in curr_set:
                result = min(result, abs(val - target))
                if result == 0:
                    return 0

            prev_set = curr_set

        return result


class SolutionBitwise:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Track bits that can be set/unset.
        """
        result = float('inf')

        # For each ending position, track possible AND values
        possible = set()

        for num in arr:
            # AND current number with all previous possibilities
            new_possible = {num}
            for val in possible:
                new_possible.add(val & num)

            # Check all values
            for val in new_possible:
                result = min(result, abs(val - target))

            possible = new_possible

        return result


class SolutionTwoPointer:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        """
        Two-pointer approach with set compression.
        """
        n = len(arr)
        result = float('inf')

        for i in range(n):
            current = arr[i]
            result = min(result, abs(current - target))

            # Extend left
            j = i - 1
            while j >= 0 and current > 0:
                current &= arr[j]
                result = min(result, abs(current - target))
                if current <= target:
                    break  # Can't get closer, AND only decreases
                j -= 1

        return result
