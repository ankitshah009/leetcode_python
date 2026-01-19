#303. Range Sum Query - Immutable
#Easy
#
#Given an integer array nums, handle multiple queries of the following type:
#Calculate the sum of the elements of nums between indices left and right
#inclusive where left <= right.
#
#Implement the NumArray class:
#    NumArray(int[] nums) Initializes the object with the integer array nums.
#    int sumRange(int left, int right) Returns the sum of the elements of nums
#    between indices left and right inclusive.
#
#Example 1:
#Input
#["NumArray", "sumRange", "sumRange", "sumRange"]
#[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
#Output
#[null, 1, -1, -3]
#
#Explanation
#NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
#numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
#numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
#numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^5 <= nums[i] <= 10^5
#    0 <= left <= right < nums.length
#    At most 10^4 calls will be made to sumRange.

from typing import List

class NumArray:
    """Prefix sum approach - O(n) preprocessing, O(1) query"""

    def __init__(self, nums: List[int]):
        # prefix[i] = sum of nums[0..i-1]
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


class NumArrayCaching:
    """Store original array and compute on demand"""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


class NumArrayAccumulate:
    """Using itertools.accumulate"""

    def __init__(self, nums: List[int]):
        from itertools import accumulate
        self.prefix = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
