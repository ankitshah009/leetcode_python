#1470. Shuffle the Array
#Easy
#
#Given the array nums consisting of 2n elements in the form
#[x1,x2,...,xn,y1,y2,...,yn].
#
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
#Example 1:
#Input: nums = [2,5,1,3,4,7], n = 3
#Output: [2,3,5,4,1,7]
#Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
#[2,3,5,4,1,7].
#
#Example 2:
#Input: nums = [1,2,3,4,4,3,2,1], n = 4
#Output: [1,4,2,3,3,2,4,1]
#
#Example 3:
#Input: nums = [1,1,2,2], n = 2
#Output: [1,2,1,2]
#
#Constraints:
#    1 <= n <= 500
#    nums.length == 2n
#    1 <= nums[i] <= 10^3

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Interleave first half with second half.
        """
        result = []
        for i in range(n):
            result.append(nums[i])      # x_i
            result.append(nums[i + n])  # y_i
        return result


class SolutionComprehension:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """Using list comprehension with zip"""
        return [val for pair in zip(nums[:n], nums[n:]) for val in pair]


class SolutionSlice:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """Using slice assignment"""
        result = [0] * (2 * n)
        result[::2] = nums[:n]   # Even indices get x values
        result[1::2] = nums[n:]  # Odd indices get y values
        return result


class SolutionInPlace:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        O(1) space solution using bit manipulation.
        Store two values in one: nums[i] = x + y * 1024
        (since nums[i] <= 1000 < 1024 = 2^10)
        """
        # Encode pairs
        for i in range(n):
            nums[i] = nums[i] | (nums[i + n] << 10)

        # Decode and place
        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] >> 10
            x = nums[i] & 1023  # 2^10 - 1

            nums[j] = y
            nums[j - 1] = x
            j -= 2

        return nums
